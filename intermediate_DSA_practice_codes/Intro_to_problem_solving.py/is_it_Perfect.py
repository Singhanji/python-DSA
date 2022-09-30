n = int(input())

for _ in range(n):
    x = int(input())
    s = 0
    for i in range(1, x):
       
        if x % i == 0:
            s += i
            print('sum', s)
            print('x', x)
        if s == x:
            print('YES')
        else:
            print('NO')
