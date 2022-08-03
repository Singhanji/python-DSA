n = input()

cnt = 0
for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        cnt += 1
print(cnt)
