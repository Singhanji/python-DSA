a = [16, 17, 4, 3, 5, 2]
n = len(a)
ans = [a[n-1]]
max_val = a[n-1]

for i in range(n-1,-1,-1):
    if (a[i] > max_val):
        max_val = a[i]
        ans.append(max_val)

print(ans)
