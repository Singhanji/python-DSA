def solve(A):
    sum = 0
    for i in range(1, 4):
        f = (A - i)
        print('f',f)
        print('A', A)
        if A == 0 or f == 0:
            return 1
        elif A == 1 or f == 1:
            return 1
        elif A == 2 or f == 2:
            return 2
        sum += f
        print(sum)
    return sum
A = 3
print(solve(A))
