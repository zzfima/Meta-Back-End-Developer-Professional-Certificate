with open("test.txt", mode="w") as fileForWrite:
    fileForWrite.writelines(["Hello python!", "\nIts Me!"])

print("\n*****read****")
with open("test.txt", mode="r") as txtFile:
    print(txtFile.read())

print("\n*****readline****")
with open("test.txt", mode="r") as txtFile:
    print(txtFile.readline())

print("\n****readlines*****")
cnt = 0
with open("test.txt", mode="r") as txtFile:
    for l in txtFile.readlines():
        print(cnt, l)
        cnt += 1
