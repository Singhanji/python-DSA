def solve(A, s, m, e):
    N = e - s + 1
    B = [0] * N
    n = len(A)
    p1 = s
    p2 = m+1
    p3 = 0

    while(p1 <= m and p2 <= e):
        if A[p1] <= A[p2]:
            B[p3] = A[p1]
            p1 += 1
            p3 += 1
        else:
            B[p3] = A[p2]
            p2 += 1
            p3 += 1
    while(p1 <= m):
        B[p3] = A[p1]
        p1 += 1
        p3 += 1
    while(p2 <= e):
        B[p3] = A[p2]
        p2 += 1
        p3 += 1

    i = s
    j = 0
    while(i <= e):
        A[i] = B[j]
        i += 1
        j += 1
    return A

A = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
s = 2
m = 6
e = 9
print(solve(A, s, m, e))


