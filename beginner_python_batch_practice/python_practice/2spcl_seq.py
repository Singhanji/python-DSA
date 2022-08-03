a = input()
n = len(a)
c = 0
ans = 0

for i in range(n-1,-1,-1):
    if a[i] == 'g':
        c += 1
    elif a[i] == 'a':
        ans += c
        ans = ans % 1000000007
print(ans)
