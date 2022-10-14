def solve(A, B):
    n = len(A)
    m = len(B)
    N = n+m
    C = [0] * N
    print(C)
    p1, p2, p3 = 0, 0, 0

    while(p1 < n and p2 < m):
        if A[p1] <= B[p2]:
            C[p3] = A[p1]
            p1 += 1
            p3 += 1
        else:
            C[p3] = B[p2]
            p3 += 1
            p2 += 1

    while(p1 < n):
        C[p3] = A[p1]
        p1 += 1
        p3 += 1
    while(p2 < m):
        C[p3] = B[p2]
        p2 += 1
        p3 += 1
    
    return C

A = [7, 10, 11, 14]
B = [3, 8, 9]
print(solve(A,B))
