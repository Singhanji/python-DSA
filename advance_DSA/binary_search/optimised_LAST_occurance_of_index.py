# Given a sorted array find last occurance array index of the given element.
# Optimised Approach
# TC: O(logN), SC: O(1) 

def solve(A,k):
    n = len(A)
    l, h = 0, n-1
    ans = -1
    while(l <= h):
        m = (l+h)//2
        if A[m] == k:
            ans = m
            l = m+1
        elif A[m] > k:
            h = m-1
        else:
            l = m+1
    return ans

A = [-5, -5, -3, 0, 0, 1, 1, 5, 5, 5, 5, 5, 5, 5, 8, 10, 10, 15, 15]
k = 10
print(solve(A,k))
