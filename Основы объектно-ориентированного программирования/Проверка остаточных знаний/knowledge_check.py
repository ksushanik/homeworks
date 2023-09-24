import timeit

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
        # elif choice == "11"
        # elif choice == "12"
        # elif choice == "13"
        # elif choice == "14"
        # elif choice == "15"
        # elif choice == "16"
        # elif choice == "17"
        # elif choice == "18"
        # elif choice == "19"
        elif choice == "q":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

        print()


if __name__ == "__main__":
    main()
