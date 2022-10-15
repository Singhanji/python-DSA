# Given a sorted arr[N] elements, find floor of given number k(greatest element <= k) in array.
# Brute Force Approach
# TC: O(N), SC: O(1)

def solve(A,k):
    ans = -float('inf')
    n = len(A)
    for i in range(n):
        if A[i] <= k:
            ans = A[i]
    return ans

A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
k = 24
print(solve(A,k))