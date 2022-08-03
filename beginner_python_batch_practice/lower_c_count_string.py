n = input()

cnt = 0

for i in n:
    if ord(i) >= 95 and ord(i) <= 122:
        cnt += 1
print(cnt)
