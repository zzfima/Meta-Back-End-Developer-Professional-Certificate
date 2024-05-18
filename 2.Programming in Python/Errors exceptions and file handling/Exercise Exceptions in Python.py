# IndexError
items = [1, 2, 3, 4, 5]
try:
    item = items[6]
    print(item)
except IndexError:
    print("Item does not exist in the list")
except Exception as e:
    print(e, " something goes wrong")


# ZeroDivisionError
def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0


ans = divide_by(40, 0)
print(ans)


# FileNotFoundError
try:
    with open("file_does_not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file could not be found")
