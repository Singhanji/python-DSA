# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
# NOTE:A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
# Brute Approach
# TC: O(N), SC = O(1)

def solve(A,B):
    n = len(A)
    for i in range(n):
        if A[i] == B:
            idx = i
    return idx

A = [3, 9, 10, 20, 17, 5, 1]
B = 20
print(solve(A,B))