# Brute Force Approach 
# Given a sorted Array[N], search if k is present or not.
# TC: O(N), SC: O(1)
# Not a good approach for big numbers or large constraints


def solve(A,k):
    
    for i in A:
        if i == k:
            return True
    return False

A = [3, 6, 9, 12, 14, 19, 20, 23, 25, 27]
k = 12
print(solve(A,k))    