"""
Условие:
Напишите программу, которая использует словарь для хранения пар "слово-перевод". 
Программа должна принимать список слов и возвращать их переводы. Если слово отсутствует в словаре, 
программа должна возвращать "Перевод не найден".
"""

dictionary = {
    "cat": "кот",
    "dog": "собака",
    "bird": "птица"
}


words = ["cat", "lion", "bird"]

def translation_of_words(words: list, dictionary : set) -> list:
    translations = []
    for word in words:
        if word in dictionary:
            translations.append(dictionary[word])
        else:
            translations.append('Перевод не найден')
    return translations




print(translation_of_words(words, dictionary))


"""
def add_to_dictionary(word, translation):
    if word not in dictionary:
        dictionary[word] = {f'{word}' : translation}
        print(f'{word} теперь в словаре')
    else:
        print(f'{word} уже в словаре')

"""