# multiply by 2
# using list comprehension


data = [3, 7, 3, 6, 9, 11, 23, 8, 4]
new_list = [x * 2 for x in data]
print(*new_list)
# using map
new_list = map(lambda x: x * 2, data)
print(*new_list)

# find numbers, divided by 4
# using list comprehension
new_list = [x for x in data if x % 4 == 0]
print(*new_list)
# using filter
new_list = filter(lambda x: x % 4 == 0, data)
print(*new_list)

# find numbers divided by 9 in range
# using list comprehension
new_list = [x for x in range(100) if x % 9 == 0]
print(*new_list)
# using filter
new_list = filter(lambda x: x % 9 == 0, range(100))
print(*new_list)
