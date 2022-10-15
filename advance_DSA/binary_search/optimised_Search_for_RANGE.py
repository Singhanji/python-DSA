# Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].
# OPTIMISED APPROACH
# TC: O(logN), SC: O(1)

def solve(A, B):
    ans = [-1,-1]
    n = len(A)
    l, h = 0, n-1

    while(l <= h):
        m = (l+h)//2
        if A[m] == B:
           ans[0] = m
           h = m-1
        elif A[m] < B:
            l = m+1
        else:
            h = m-1
        
    l, h = 0, n-1
    while(l <= h):
        m = (l+h)//2
        if A[m] == B:
            ans[1] = m
            l = m+1
        elif A[m] < B:
            l = m+1
        else:
            h = m-1
        
    return ans

A = [5, 7, 7, 8, 8, 10]
B = 8
#A = [5, 17, 100, 111]
#B = 3
print(solve(A,B))                                                                      


   