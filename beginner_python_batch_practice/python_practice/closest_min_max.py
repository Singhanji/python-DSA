a = [1, 2, 3, 1, 3, 4, 6, 4, 6, 3]

n = len(a)
min_v = a[0]
max_v = a[0]
ans = n

for i in range(n):
    if a[i] < min_v:
        min_v = a[i]
    elif a[i] > max_v:
        max_v = a[i]

#print("min:", min_v)
#print("max: ",max_v)

if (max_v == min_v):
    print(1)

for i in range(n):
    if a[i] == min_v:
        for j in range(1,n):
            if a[j] == max_v:
                ans = min(ans, j-i+1)
                break

    elif a[i] == max_v:
        for k in range(1,n):
            if a[j] == min_v:
                ans = max(ans, j-i+1)
                break
print(ans)

