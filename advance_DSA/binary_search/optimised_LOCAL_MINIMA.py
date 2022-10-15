# Given Unsorted array[N] distinct elements, return any local minima. 
# An element is said to be local minima, if it is less than it's adjacent elements.
# SC: O(N), SC: O(1)

def local(A):
    n = len(A)
    l, h = 1, n-2
    if A[0] < A[1]:
        return A[0]
    if A[n-1] < A[n-2]:
        return A[n-1]
    while(l <= h):
        m = (l+h)//2
        if A[m] < A[m-1] and A[m] < A[m+1]:
            return A[m]
        if A[m] > A[m-1]:
            h = m-1
        else:
            l = m+1
    return A[m]

A = [9, 8, 7, 3, 6, 4, 1, 5, 2]
print(local(A))
