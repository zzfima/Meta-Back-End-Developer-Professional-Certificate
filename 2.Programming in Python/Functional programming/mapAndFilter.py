def checkSign(i: int) -> str:
    if i >= 0:
        return "pos: " + str(i)
    else:
        return "neg: " + str(i)


# arrange values with their polarity
addedList = map(checkSign, [1, 2, -3, 4, -5])
print(*addedList)

# return all numbers multiplicated by 20
addedList = map(lambda i: i * 10, [1, 2, -3, 4, -5])
print(*addedList)

# take only positive numbers
addedList = filter(lambda i: i >= 0, [1, 2, -3, 4, -5])
print(*addedList)
