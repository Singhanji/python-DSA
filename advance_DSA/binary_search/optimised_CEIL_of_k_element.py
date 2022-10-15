# Given a sorted array[N] elements, find ceil of a given num k, greatest element <= k in array.
# Optimised Approach
# TC: O(logN), SC: O(1)

def solve(A,k):
    n = len(A)
    l, h = 0, n-1
    ans = -1
    while(l <= h):
        m = (l+h)//2
        if A[m] == k:
            return ans
            
        if A[m] > k:
            ans = A[m]
            h = m-1
        else:
            l = m+1
    return ans


A = [-5, 2, 3, 6, 9, 10, 11, 14, 18]
k = 24
print(solve(A,k))