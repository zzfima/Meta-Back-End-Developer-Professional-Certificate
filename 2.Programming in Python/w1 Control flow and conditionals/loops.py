print("**1**")
text = "hello"
for c, i in enumerate(text):
    print("element at ", c, " is character ", i)

print("**2**")
cnt = 0
while cnt < 5:
    if cnt == 1:
        cnt = 2
        continue
    print(cnt)
    if cnt == 2:
        break
    cnt += 1

print("**3**")
for i in range(5):
    print(i)
