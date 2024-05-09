with open("test.txt", mode="w") as fileForWrite:
    fileForWrite.write("Hello python!")

with open("test.txt", mode="r") as txtFile:
    print(txtFile.read())
