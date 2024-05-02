workers = ["Alex", "Moshe"]
salad = [1, 2, 3, "Pepper"]

print(workers)
print(salad)

list1 = [1, 2, 3, 4]
print(list1)
print(*list1)
print(*list1, sep=", ")

list1.insert(len(list1), 5)
print(*list1)

list1.extend([6, 7])
print(*list1)

list1.pop(2)
print(*list1)

list1.remove(2)
print(*list1)

for x in list1:
    print(x)

list1.append(44)
print(*list1)