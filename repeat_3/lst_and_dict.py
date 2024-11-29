# списки
l1 = [1, 5, 4, 6, "asd", True]
print(l1[1], l1[-1])

for i in range(len(l1)):
    print(l1[i], end=" ")
print()

for v in l1:
    print(v, end=" ")
print()


# словарики
d = dict()

d1 = {}
# ключ - либо число, либо строка
# значение - любой тип данных
d3 = {"key1": l1, "key2": 321, 1: "val1", "qwe": "ttt"}
print(d3["key1"], d3[1])



for key, val in d3.items():
    print(f"{key}: {val}\t|\t", end=" ")
print()



d3["new_key"] = "new_val" # новая пара -ключ: значение
d3["qwe"] = "new_qwe_val" # изменение значения по ключу
del d3["key2"] # удаление пары по ключу

for key in d3:
    print(f"{key}: {d3[key]}\t|\t", end=" ")
print()