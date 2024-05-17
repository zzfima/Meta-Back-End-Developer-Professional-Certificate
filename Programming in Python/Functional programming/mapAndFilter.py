def checkSign(i: int) -> str:
    if i >= 0:
        return "pos: " + str(i)
    else:
        return "neg: " + str(i)


addedList = map(checkSign, [1, 2, -3, 4, -5])
print(*addedList)


addedList = map(lambda i: i * 10, [1, 2, -3, 4, -5])
print(*addedList)
