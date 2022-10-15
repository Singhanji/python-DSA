# Given a sorted array[N] elements, find ceil of a given num k, greatest element <= k in array.
# Brute Force Approach
# TC: O(N), SC: O(1)

def solve(A,k):
    n = len(A)
    for i in range(n):
        if A[i] == k:
            return k
        if A[i] > k:
            return A[i]
    return -1
A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
k = 100
print(solve(A,k))