# Bubble Sort
# Given Ar[N], we can only swap adjacent elements, sort the array.
# TC: O(N*N), SC: O(1)
# It is Stable Algorithm

def bubble(A):
    n = len(A)

    for i in range(n):
        c = 0
        for j in range(n-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                c += 1
        if c == 0:
            break
    return A

A = [2, 8, 4, -1, 6, 7, 5, 10, -1]
print(bubble(A))