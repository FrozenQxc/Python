s = input("Введите строку: ")
n = len(s)

for i in range(n):
    if i == 2:
        continue
    if s[i] == "c":
        print("Найден символ 'c'")
    print(s[i], end="")
print("\nДлина строки:", n-1)
