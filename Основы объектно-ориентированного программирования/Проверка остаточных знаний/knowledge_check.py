import random
import timeit
import tkinter as tk

import memory_profiler

from tasks import TASKS


def swap_variables(a=1, b=2, c=3):
    a, b, c = b, c, a
    return a, b, c


def get_sum_of_numbers():
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка! Введите числа заново.")
    return num1 + num2


def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка! Введите корректное число.")


def calculate_power(x):
    return x ** 5


def calculate_power_mult(x):
    res = 1
    for _ in range(5):
        res *= x
    return res


def is_fibonacci_number(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n


def count_divisors(N):
    res = []
    for num in range(1, N + 1):
        divisors = 0
        sqrt_num = int(num ** 0.5)
        for i in range(1, sqrt_num + 1):
            if num % i == 0:
                divisors += 2
        if sqrt_num ** 2 == num:
            divisors -= 1
        res.append((num, divisors))
    return res


def time_memo(func, value):
    # Измерение памяти
    memory_usage = memory_profiler.memory_usage((func, (value,)))
    print(f"Использование памяти: {max(memory_usage)} МБ")

    # Измерение времени выполнения
    execution_time = timeit.timeit(lambda: func(value), number=1)
    print(f"Время выполнения: {execution_time} секунд")


def find_pythagorean_triplets(N, M):
    triplets = []
    for a in range(N, M + 1):
        for b in range(a, M + 1):
            c = (a ** 2 + b ** 2) ** 0.5
            if c.is_integer() and c <= M:
                triplets.append((a, b, int(c)))
    return triplets


def find_numbers_divisible_by_digits(N, M):
    result = []
    for num in range(N, M + 1):
        digits = str(num)
        for digit in digits:
            if int(digit) == 0 or num % int(digit) != 0:
                break
        else:
            result.append(num)
    return result


def find_perfect_numbers(N):
    perfect_numbers = []
    number = 2

    while len(perfect_numbers) < N:
        divisors = [1]

        for i in range(2, number // 2 + 1):
            if number % i == 0:
                divisors.append(i)

        if sum(divisors) == number:
            perfect_numbers.append(number)

        number += 1

    return perfect_numbers


def get_last_element_by_index(array):
    last_element = array[-1]
    return "Последний элемент (индексация): ", last_element


def get_last_element_by_slice(array):
    last_element = array[-1:]
    return "Последний элемент (срез): ", last_element


def get_last_element_by_length(array):
    last_element = array[len(array) - 1]
    return "Последний элемент (использование длины массива): ", last_element


def recursive_sum(array, index):
    if index == len(array) - 1:
        return array[index]
    else:
        return array[index] + recursive_sum(array, index + 1)


def main():
    while True:
        print("Выберите задачу c 1 по 19:")
        print("q. Выход")

        choice = input("Введите номер задачи: ")
        print(TASKS[int(choice)] if choice.isdigit() else "Закончили")

        if choice == "1":
            a, b, c = swap_variables()
            print(f"a={a}, b={b}, c={c}")

        elif choice == "2":
            print("Сумма чисел равна:", get_sum_of_numbers())

        elif choice == "3":
            sum_nums = 0
            while True:
                try:
                    n = int(input("Введите количество чисел: "))
                    if n <= 0:
                        print("Ошибка! Введите положительное число.")
                        continue
                    for _ in range(n):
                        num = get_number_input("Введите число: ")
                        sum_nums += num
                    break
                except ValueError:
                    print("Ошибка! Введите корректное число.")

            print("Сумма чисел равна:", sum_nums)

        elif choice == "4":
            x = float(input("Введите число от 0 до 100: "))

            if 0 <= x <= 100:
                result = calculate_power(x)
                print(f"Значение {x} в степени 5 равно {result}")
            else:
                print("Ошибка! Введите число от 0 до 100.")

        elif choice == "5":
            x = float(input("Введите число от 0 до 100: "))

            if 0 <= x <= 100:
                result = calculate_power(x)
                result_2 = calculate_power_mult(x)

                print(f"Значение {x} в степени 5 равно {result}")
                time_memo(calculate_power, x)

                print(f"Значение {x} в степени 5 равно {result_2}")
                time_memo(calculate_power_mult, x)

            else:
                print("Ошибка! Введите число от 0 до 100.")

        elif choice == "6":
            number = int(input("Введите число от 0 до 250: "))

            if 0 <= number <= 250:
                if is_fibonacci_number(number):
                    print(f"Число {number} принадлежит числам Фибоначчи.")
                else:
                    print(f"Число {number} не принадлежит числам Фибоначчи.")
            else:
                print("Ошибка! Введите число от 0 до 250.")

        elif choice == "7":
            month = int(input("Введите номер месяца (от 1 до 12): "))

            if month == 12 or month == 1 or month == 2:
                season = "зима"
            elif month == 3 or month == 4 or month == 5:
                season = "весна"
            elif month == 6 or month == 7 or month == 8:
                season = "лето"
            elif month == 9 or month == 10 or month == 11:
                season = "осень"
            else:
                season = "некорректный месяц"

            print(f"Время года для месяца {month} - {season}.")

            month = int(input("Введите номер месяца (от 1 до 12): "))

            seasons = {
                (12, 1, 2): "зима",
                (3, 4, 5): "весна",
                (6, 7, 8): "лето",
                (9, 10, 11): "осень"
            }

            for months, season in seasons.items():
                if month in months:
                    print(f"Время года для месяца {month} - {season}.")
                    break
            else:
                print("Некорректный месяц.")

        elif choice == "8":
            n = int(input("Введите число N: "))
            print(f"Сумма чисел = {sum(range(n))}")
            print(f"Сумма четных чисел = {sum(range(2, n, 2))}")
            print(f"Сумма чисел = {sum(range(1, n, 2))}")

        elif choice == "9":
            n = int(input("Введите число N: "))
            print(count_divisors(n))
            time_memo(count_divisors, n)

        elif choice == "10":
            n = int(input("Введите значение N: "))
            m = int(input("Введите значение M: "))

            triplets = find_pythagorean_triplets(n, m)
            for triplet in triplets:
                print(triplet)

        elif choice == "11":
            n = int(input("Введите начальное значение N: "))
            m = int(input("Введите конечное значение M: "))

            numbers = find_numbers_divisible_by_digits(n, m)
            print("Числа, делящиеся на каждую из своих цифр:")
            print(numbers)

        elif choice == "12":
            n = int(input("Введите количество совершенных чисел (N < 5): "))

            if n < 5:
                numbers = find_perfect_numbers(n)
                print("Совершенные числа:")
                print(numbers)
            else:
                print("Некорректное значение N. Введите значение меньше 5.")

        elif choice == "13":
            my_array = [10, 20, 30, 40, 50]

            for func in [get_last_element_by_index, get_last_element_by_slice, get_last_element_by_length]:
                print(*func(my_array))
                time_memo(func, my_array)

        elif choice == "14":
            my_array = [5, 10, 15, 20, 25, 30]
            print(my_array[::-1])

        elif choice == "15":
            my_array = [10, 20, 30, 40, 50]
            result = recursive_sum(my_array, 0)

            print("Сумма элементов массива:", result)

        elif choice == "16":
            def convert():
                rubles = float(entry.get())
                dollars = rubles / 100  # Предполагаем курс 1 доллар = 100 рублей
                result_label.config(text=f"Сумма в долларах: {dollars:.2f}")

            # Создание окна для конвертера рублей в доллары
            window1 = tk.Tk()
            window1.title("Конвертер рублей в доллары")

            # Создание метки и поля ввода
            label1 = tk.Label(window1, text="Введите сумму в рублях:")
            label1.pack()

            entry = tk.Entry(window1)
            entry.pack()

            # Создание кнопки конвертирования
            button = tk.Button(window1, text="Конвертировать", command=convert)
            button.pack()

            # Создание метки для вывода результата
            result_label = tk.Label(window1, text="")
            result_label.pack()

            # Запуск главного цикла окна
            window1.mainloop()

        elif choice == "17":
            def convert_to_dollars():
                rubles = float(entry.get())
                dollars = rubles / 75  # Предполагаем курс 1 доллар = 75 рублей
                result_label.config(text=f"Сумма в долларах: {dollars:.2f}")

            def convert_to_rubles():
                dollars = float(entry.get())
                rubles = dollars * 75  # Предполагаем курс 1 доллар = 75 рублей
                result_label.config(text=f"Сумма в рублях: {rubles:.2f}")

            def convert():
                if mode.get() == 1:
                    convert_to_dollars()
                elif mode.get() == 2:
                    convert_to_rubles()

            def update_label():
                if mode.get() == 1:
                    label.config(text="Введите сумму в рублях:")
                elif mode.get() == 2:
                    label.config(text="Введите сумму в долларах:")

            # Создание окна для конвертера валют
            window2 = tk.Tk()
            window2.title("Конвертер валют")

            # Создание метки и поля ввода
            label = tk.Label(window2, text="Введите сумму в рублях:")
            label.pack()

            entry = tk.Entry(window2)
            entry.pack()

            # Создание метки для вывода результата
            result_label = tk.Label(window2, text="")
            result_label.pack()

            # Создание переменной для выбора режима конвертации
            mode = tk.IntVar()
            mode.set(1)  # По умолчанию выбран режим конвертации в доллары

            # Создание радиокнопок для выбора режима конвертации
            radio_to_dollars = tk.Radiobutton(window2, text="Рубли в доллары", variable=mode, value=1,
                                              command=update_label)
            radio_to_dollars.pack()

            radio_to_rubles = tk.Radiobutton(window2, text="Доллары в рубли", variable=mode, value=2,
                                             command=update_label)
            radio_to_rubles.pack()

            # Создание кнопки конвертирования
            button_convert = tk.Button(window2, text="Конвертировать", command=convert)
            button_convert.pack()

            # Запуск главного цикла окна
            window2.mainloop()

        elif choice == "18":
            n = int(input("Введите значение n: "))
            m = int(input("Введите значение m: "))

            if n < 5 or n > 20 or m < 5 or m > 20:
                print("Ошибка! Значения должны быть в диапазоне от 5 до 20.")
                exit()

            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    print(f"{i} * {j} = {i * j}")

        elif choice == "19":
            # Определение размера поля
            rows = 10
            cols = 10

            # Создание пустого поля
            field = [[' ' for _ in range(cols)] for _ in range(rows)]

            # Заполнение поля кораблями
            for _ in range(5):
                # Генерация случайных координат для корабля
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)

                # Размещение корабля на поле
                field[row][col] = 'X'

            # Вывод поля в консоль
            for row in field:
                print(' '.join(row))

        elif choice == "q":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

        print()


if __name__ == "__main__":
    main()
