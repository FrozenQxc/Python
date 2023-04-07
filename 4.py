import math
import random

print("Операции: +, -, /, *, ** (возведение в степень), mod (модуль), rand (рандомное число), fact (факториал), acos (арккосинус)")

while True:

    choice = input("Введите операцию: ")
    # Метод split используется для разбиения строки на список подстрок по определенному разделителю. В данном случае разделитель - это пробел.
    # Метод map делает число вещественным
    if choice == "+":
        num1, num2 = map(float, input("Введите два числа через пробел: ").split())
        print(num1 + num2)
        break

    elif choice == "-":
        num1, num2 = map(float, input("Введите два числа через пробел: ").split())
        print(num1 - num2)
        break

    elif choice == "*":
        num1, num2 = map(float, input("Введите два числа через пробел: ").split())
        print(num1 * num2)
        break

    elif choice == "/":
        num1, num2 = map(float, input("Введите два числа через пробел: ").split())
        if num2 != 0:
            print(num1 / num2)
            break
        else:
            print("Ошибка: деление на ноль.")

    elif choice == "**":
        num1, num2 = map(float, input("Введите число и степень через пробел: ").split())
        print(num1 ** num2)
        break

    elif choice == "mod":
        num = float(input("Введите число: "))
        result = abs(num)
        print("Результат:", result)
        break

    elif choice == "rand":
        low, high = map(int, input("Введите нижнюю и верхнюю границы через пробел: ").split())
        result = random.uniform(low, high)
        print("Результат:", result)
        break

    elif choice == "fact":
        num = int(input("Введите число: "))
        if num >= 0:
            print(math.factorial(num))
            break
        else:
            print("Ошибка: факториал отрицательного числа не существует.")

    elif choice == "acos":
        num = float(input("Введите число: "))
        if -1 <= num <= 1:
            print(math.acos(num))
            break
        else:
            print("Ошибка: введенное число должно быть в диапазоне от -1 до 1.")

    else:
        print ("Возникла ошибка.Try again")
