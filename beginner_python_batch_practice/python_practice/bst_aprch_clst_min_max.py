#a = [1, 6, 4, 6, 5, 1, 5, 2, 6, 4, 4, 2, 1]
a = [ 343, 291, 963, 165, 152 ]

#a = map(list(int, input().split()))
n = len(a)
min_v = a[0]
max_v = a[0]

for i in range(n):
    if a[i] < min_v:
        min_v = a[i]
    elif a[i] > max_v:
        max_v = a[i]

if (max_v == min_v):
    print(1)

ans = n
min_I = -1
max_I = -1

for i in range(n-1,-1,-1):
    if a[i] == min_v:
        min_I = i
        if max_I != -1:
            l = max_I - min_I + 1
            ans = min(ans,l)
    elif a[i] == max_v:
        max_I = i
        if min_I != -1:
            l = min_I - max_I + 1
            ans = min(ans, l)

print(ans)





