e = "apple banana apple grape banana apple"
"""
Условие:
Напишите функцию, которая принимает строку текста и возвращает словарь, где ключами являются уникальные слова, 
а значениями — частота их появления в тексте.
"""



"""
words = input().split()
# print(*words)
for word in words:
    d = {word : words.count(word)}
    if  not word in d:
        d.update({f'{word}' : words.count(f'{word}')})
print(d)
"""


"""
words = input().split()
keys = []
print(*words)
for i in range(len(words)):
    if not words[i] in keys:
        keys.append(f'{words[i]}')
for word in keys:
    word_and_count = {f'{word}' : words.count(f'{word}')}

print(word_and_count)
"""



# рабочий
"""
def word_and_count(text):
    words = text.split()
    d = {}
    for word in words:
        if not word in d:
            d[word] = 1
        else:
            d[word] += 1
    return d

print(word_and_count(input()))
"""

def word_and_count_1(text):
    words = text.split()
    unique_words = []
    c = []
    w_c = [] # двойной список
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
            c.append(1)
        else:
            id = unique_words.index(word)
            c[id] += 1
    # w_c = [unique_words, c] # ошибка
    for i in range(len(unique_words)):
        w_c.append([unique_words[i], c[i]])
    return w_c


print(word_and_count_1(input()))