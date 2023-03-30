import math
import random

while True:
    print("Операции: +, -, /, *, ** (возведение в степень), mod (модуль), rand (рандомное число), fact (факториал), acos (арккосинус)")

    choice = input("Введите операцию: ")

    if choice == "+":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(num1 + num2)
        break

    elif choice == "-":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(num1 - num2)
        break

    elif choice == "/":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(num1 / num2)
        break

    elif choice == "*":
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        print(num1 * num2)
        break

    elif choice == "**":
        num1 = float(input("Введите число: "))
        num2 = float(input("Введите степень: "))
        print(num1 ** num2)
        break

    elif choice == "mod":
        num = float(input("Введите число: "))

        result = abs(num)
        print("Результат:", result)
        break

    elif choice == "rand":
        low = int(input("Введите нижнюю границу: "))
        high = int(input("Введите верхнюю границу: "))

        result = random.uniform(low, high)
        print("Результат:", result)
        break

    elif choice == "fact":
        num = int(input("Введите число: "))
        print(math.factorial(num))
        break

    elif choice == "acos":
        num = float(input("Введите число: "))
        print(math.acos(num))
        break

    else:
        print ("Возникла ошибка.Try again")