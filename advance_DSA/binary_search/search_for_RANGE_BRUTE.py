# Given a sorted array of integers A(0 based index) of size N, find the starting and the ending position of a given integer B in array A.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Return an array of size 2, such that the first element = starting position of B in A and the second element = ending position of B in A, if B is not found in A return [-1, -1].
# BRUTE FORCE APPROACH
# TC: O(N), SC: O(1)

def solve(A, B):
    n = len(A)
    ans = []
    for i in range(n):
        if A[i] == B:
            ans.append(i)
            break
    for j in range(n-1,-1,-1):
        if A[j] == B:
            ans.append(j)
            break
    if len(ans) == 0:
        return [-1,-1]
    return ans

A = [5, 7, 7, 8, 8, 10]
B = 3
print(solve(A,B))