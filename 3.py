text = input("Введите текст: ")

# Разбиваем текст на слова и создаем словарь для подсчета количества повторений
words = text.split()
word_count = {}

# Подсчитываем количество повторений каждого слова
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Находим наиболее часто встречающееся слово
most_common_word = max(word_count, key=word_count.get)

# Находим самое длинное слово
longest_word = max(words, key=len)

# Выводим результаты
print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)
