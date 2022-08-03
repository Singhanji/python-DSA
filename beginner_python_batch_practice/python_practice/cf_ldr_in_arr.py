#a = [10, 8, 9, 2]
a = list(map(int, input().split()))
n = len(a)
c = 1

for i in range(n-1,-1,-1):
    print("i", i)
    max = a[i]
    print("max:", max)
    if a[i-1] > max:
        max = a[i]
        c += 1
print(c)
