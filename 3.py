text = input("Введите текст: ")
words = text.split()

word_count = {}

for word in words:
    word_count.setdefault(word, 0)
    word_count[word] += 1

most_common_word = max(word_count, key=word_count.get)

longest_word = max(words, key=len)

print(f"Наиболее часто встречающееся слово: {most_common_word}")
print(f"Самое длинное слово: {longest_word}")

