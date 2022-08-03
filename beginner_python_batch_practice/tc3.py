def solve():
    n = int(input())
    i = 1
    print("i: ", i)
    print('---------------------------')
    while i < n:
        x = i
        print("x: ", x)
        print('--------------------------')
        while x > 0:
            x -= 1
            print("x where x in decreasing: ", x)
            print('---------------------------------------')
        i += 1
        print("i where i is increasing: ", i)

solve()
