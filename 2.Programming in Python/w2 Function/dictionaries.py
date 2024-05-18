# initialize dictionary
drinks = {1: "coffee", 2: "tea", 3: "juice"}
print(drinks[1])

# update dictionary
drinks[1] = "espresso"
print(drinks[1])

# delete dictionary key value
del drinks[1]

# print all keys
for x in drinks.keys():
    print(x)

# print all values
for x in drinks.values():
    print(x)

# print all values and keys
for k, v in drinks.items():
    print(k, " is ", v)


print(type(drinks).__name__)
