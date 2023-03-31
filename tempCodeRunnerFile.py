string = input("Введите строку: ")
length = len(string)

for index, char in enumerate(string):
    if char == "c":
        print("Найден символ 'c'")
        continue
    if index != 2:
        print(char, end="")

print("\nДлина строки:", length)
