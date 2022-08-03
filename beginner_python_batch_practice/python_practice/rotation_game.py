a = list(map(int, input().split()))
k = int(input())

n = len(a)

k = k % n

for i in range(1,n):
    if i < k:
        print(a[n+i-k],end=' ')
    else:
        print(a[i-k], end=' ')

    print("\n")
