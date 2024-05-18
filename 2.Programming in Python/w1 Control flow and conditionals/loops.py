text = "hello"

for c, i in enumerate(text):
    print("element at ", c, " is character ", i)

cnt = 0

while cnt < 5:
    print(cnt)
    if cnt == 2:
        break
    cnt += 1

for i in range(5):
    print(i)
