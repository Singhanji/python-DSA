def solve(A):
    n = len(A)
    i = 0
    while(i<n):
        if A[i] < 1 or A[i] > n or A[i] == i+1:
            i += 1
        else:
            cind = A[i] - 1
            if A[i] == A[cind]:
                i += 1
            else:
                A[i],A[cind] = A[cind],A[i]
    for i in range(n):
        if A[i] != i+1:
            return i+1
    return n+1


#A = [9, -14, 6, -7, 5, 12, 2, 3, 8, 1]
#A = [1, 2, 0]
#A = [3, 4, -1, 1]
A = [-8, -7, -6]
print(solve(A))