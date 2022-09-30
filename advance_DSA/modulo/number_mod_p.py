# Given 1 number in arr[N], calculate number % p

def solve(A, p):
    n = len(A)
    res = 0
    x = 1
    for i in range(n-1,-1,-1):
        d = A[i] % p
        res = (res + (d * x) % p) % p
        x = (x * 10) % p

    return res

A = [3, 2, 6, 4, 9]
p = 5
print(solve(A, p))
