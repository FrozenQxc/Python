string = input("Введите строку: ")
length = len(string)
count = 0

for index, char in enumerate(string):
    if char == "c":
        count += 1
        print("Найден символ 'c'")
        continue

print("\nКоличество символов 'c':", count)
print("Длина строки:", length)