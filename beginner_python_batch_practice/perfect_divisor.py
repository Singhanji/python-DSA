n = int(input())

for x in range(n):
    m = int(input())
    
    c = 0
    for i in range(1,m):
        if m % i == 0:
            c += i
    
    if c == m:
        print("YES")
    else:
        print("NO")
