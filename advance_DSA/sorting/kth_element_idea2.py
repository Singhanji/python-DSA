# Given ar[N] elements, find kth smallest element (return ar[k-1] index element, when array is sorted.)
# Idea 2: selection Sort- Sort the array and get k-1th element 
# TC: O(N*N)

def solve(A, k):
    A = list(A)
    n = len(A)
    for i in range(n):
        min = A[i]
        idx = i
        for j in range(i, n):
            if A[j] < min:
                min = A[j]
                idx = j
        A[idx],A[i] = A[i],A[idx]

    return A[k-1]


#A = (2, 8, 5, -1, 6, 7, 4, 10, -1)
A = (2, 1, 4, 3, 2)
k = 3
print(solve(A, k))