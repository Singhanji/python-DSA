from regex import E


def querySum(A):
    n = len(A)
    Q = int(input())
    while Q > 0:
        
        l = int(input())
        r = int(input())
        Q -= 1
        sum = 0
        for i in range(l, r+1):
            print(A[i])
            sum += A[i]
        print('sum: ', sum)
    return sum

A = [-3, 6, 2, 4, 5, 2, 8, -9, 3, 1]
print(querySum(A))

