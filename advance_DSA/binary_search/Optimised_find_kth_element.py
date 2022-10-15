# Brute Force Approach 
# Given a sorted Array[N], search if k is present or not.
# TC: O(logN), SC: O(1)
# Best approach for larger inputs too

def solve(A,k):
    n = len(A)
    l, h = 0, n-1
    while(l<=h):
        m = (l+h)//2
        if A[m]==k:
            return True
        if A[m] < k:
            l = m+1
        else:
            h = m-1
    return False

A = [3, 6, 9, 12, 14, 19, 20, 23, 25, 27]
k = 21
print(solve(A,k))