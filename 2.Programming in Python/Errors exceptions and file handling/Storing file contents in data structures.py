import random


with open("petnames.txt", mode="r") as f:
    content = f.read()
    contentList = content.split("\n")
    print(contentList)
    print(random.choice(contentList))
