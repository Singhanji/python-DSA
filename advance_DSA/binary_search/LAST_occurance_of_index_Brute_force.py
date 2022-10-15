# Given a sorted array find last occurance array index of the given element.
# BRUTE Force Approach
# TC: O(N), SC: O(1) 

def solve(A,k):
    idx = -1
    n = len(A)
    for i in range(n-1,-1,-1):
        if A[i] == k:
            idx = i
            return idx
    return idx

A = [-5, -5, -3, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 8, 10, 10, 15, 15]
k = 0
print(solve(A,k))
