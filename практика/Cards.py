import random


print('Привет мужик! У меня есть 3 карты, выбири одну из них и узнай свою судьбу!')
card = int(input("Выберите карту от 1-3: "))

if card == 1:
    print('Ты выбрал первую карту! Ты выйграл золото!')
elif card == 2:
    print('Ты выбрал вторую карту! Ты выйграл меч!')
elif card == 3:
    print('Ты выбрал третью карту! Ты ничего не выиграл :( ')
else:
    print('Необходимо выбрать число от 1 до 3')



print("Угадай магическое число!")

magic = random.randint(1, 100)

while True:
    num = int(input("Введите число: "))

    if num < magic:
        print(f'Число больше, чем {num}')
    elif num > magic:
        print(f'Число меньше, чем {num}')
    elif num == magic:
        break

print('Ты угадал!')


print("Теперь я угадаю твое число. Загадывай!")
print("Загадайте число от 1 до 100, а я попробую угадать.")
min_num = 1
max_num = 100
guesses = 0

while True:
    guess = random.randint(min_num, max_num)
    print("Мой вариант:", guesses)
    answer = input("Больше, меньше или угадал?(</>/=): ").lower()
    guesses += 1
    if answer == '=':
        print(f"Ура! Я угадал число {guesses}, за {guesses} попыток.")
        break
    elif answer == '<':
        max_num = guess - 1
    elif answer == '>':
        min_num = guess + 1
    else:
        print("Некорректный ответ, попробуйте еще раз.")
