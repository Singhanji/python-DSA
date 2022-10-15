# Given a sorted arr[N] elements, find floor of given number k(greatest element <= k) in array.
# Optimised solution Approach
# TC: O(logN), SC: O(1)

def solve(A,k):
    n = len(A)
    ans = float('-inf')
    l, h = 0, n-1
    while(l <= h):
        m = (l+h)//2
        if A[m] == k:
            return A[m]
        if A[m] < k:
            ans = A[m]
            l = m+1
        else:
            h = m-1

    return ans

A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
k = -7  
print(solve(A,k))