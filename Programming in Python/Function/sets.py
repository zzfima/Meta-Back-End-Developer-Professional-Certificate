s1 = {1, 2, 3, 4, 5}
print(*s1)

s1.add(6)
print(*s1)

s1.add(2)
print(*s1)

s2 = {2, 5, 7}
print("union: ", s1.union(s2))
print("diff: ", s1.difference(s2))
print("intersection: ", s1.intersection(s2))
