def insertion(A):
    n = len(A)
    for i in range(n-2, -1, -1):
        if A[i] > A[i+1]:
            A[i],A[i+1] = A[i+1],A[i]
        else:
            break
    return A

A = [2, 6, 10, 14, 20, 4]
print(insertion(A))
    