# список, словарь
# кортеж, множество

l1 = [1, 2, 3]
k1 = (1, 2, 3) # не изменяемый список
print(k1[1])

# Множества

l2 = [1, 3, 4, 2, 3, 4, 1, 5, 6, 3, 4, 1, 6, 7, 3, 5]
s = set(l1)
s = {i for i in l2}
s.add(8)
print(s)

l3 = list(s)
print(l3[-5:])

s.remove(4)
print(s)

print("-" * 20)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
u_s = s1.union(s2)
print(f"union: {u_s}")
i_s = s1.intersection(s2)
print(f"intersection: {i_s}")
d_s1 = s1.difference(s2)
print(f"difference: {d_s1}")
d_s2 = s2.difference(s1)
print(f"difference: {d_s2}")