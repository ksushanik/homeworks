import re
import socket
import csv
import ast
import datetime


# Функция для чтения реестра из файла
def read_registry(filename):
    registry_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропустим первую строку с заголовками
        for row in csv_reader:
            ips = ast.literal_eval(row[0])  # Преобразуем строку в список IP-адресов
            domains = row[1]
            urls = row[2]
            org = row[3]
            decision_number = row[4]
            decision_date = row[5]
            apply_date = row[6]
            registry_list.append((ips, domains, urls, org, decision_number, decision_date, apply_date))

    return registry_list


# Функция для проверки URL
def check_url(user_url, registry_list):
    for item in registry_list:
        # Извлекаем домен из URL и проверяем наличие в списке
        if user_url.startswith('http://' + item[1]) or user_url.startswith('https://' + item[1]):
            return f"Сайт {user_url} заблокирован. Решение {item[4]} от {item[5]} органа {item[3]}. Применено {item[6]}"
    return None


# Функция для автоматического определения IP-адреса домена
def get_ip_from_domain(user_url):
    try:
        ip_address = socket.gethostbyname(user_url)
        return ip_address
    except socket.gaierror:
        return None


# Главная функция
def main():
    registry_filename = 'register0610.csv'
    registry_list = read_registry(registry_filename)

    log_filename = 'log.txt'
    with open(log_filename, 'a', encoding='utf-8') as log_file:
        while True:
            user_input = input("Введите URL сайта для проверки (или 'exit' для завершения): ")

            if user_input.lower() == 'exit':
                break

            # Проверка валидности URL
            if not re.match(r"^(https?://)?[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})(/.*)?$", user_input):
                print("Некорректный URL.")
                continue

            # Если введенный пользователем URL, попробуем определить IP-адрес
            if not user_input.startswith('http://') and not user_input.startswith('https://'):
                user_input = 'http://' + user_input
            user_url = re.sub(r'^https?://', '', user_input)
            user_ip = get_ip_from_domain(user_url)
            if user_ip:
                print(f"IP-адрес домена {user_url}: {user_ip}")
                user_url = 'http://' + user_ip

            url_result = check_url(user_input, registry_list)
            if url_result:
                print(url_result)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_file.write(f"{timestamp}: {url_result}\n")
            else:
                print("Сайт не запрещен.")


if __name__ == "__main__":
    main()
