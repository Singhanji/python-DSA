# Given a sorted Array[N] elements, find the first occurance index of the given element.
# Brute Force Approach 
# TC: O(N), SC: O(1) 

def solve(A,k):
    idx = -1
    n = len(A)
    for i in range(n):
        if A[i] == k:
            idx = i
            return idx
    return idx


A = [-5, -5, -3, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 8, 10, 10, 15, 15]
k = 20
print(solve(A,k))
