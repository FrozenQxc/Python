string = input("Введите строку: ")
length = len(string)
count = 0

for index, char in enumerate(string):
    if index == 2:
        continue
    elif char == "c":
        count += 1
        print("Строка содержит символ 'c'")

    if index < length-1:
        print(char, end="")

        if index == length - 3:
            print("\nПропущен третий символ:", string[2], end="")

print("\nКоличество символов 'c':", count)
print("Длина строки:", length)