def solve(A):
    A.sort()
    n = len(A)

    for i in range(n-1):
        if A[i] == A[i+1] - 1:
            continue
        return 0
    return 1

#A = [3, 2, 1, 4, 5]
A = [1, 3, 2, 5]
print(solve(A))

