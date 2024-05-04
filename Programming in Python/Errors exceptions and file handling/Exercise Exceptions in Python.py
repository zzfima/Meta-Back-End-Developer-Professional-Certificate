# Starter code
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except IndexError:
    print("Item does not exist in the list")
except Exception as e:
    print(e, " something goes wrong")
