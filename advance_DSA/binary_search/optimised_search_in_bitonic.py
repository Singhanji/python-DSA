# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
# NOTE:A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
# Brute Approach
# TC: O(N), SC = O(1)

def solve(A,B):
    n = len(A)
    low = 0
    high = n-1

    while(low <= high):
        mid = (low + high) // 2
        if A[mid] == B:
            return 1
        if A[mid] < B:
            low = mid + 1
        else:
            high = mid - 1
    return 0

#A = [3, 9, 10, 20, 17, 5, 1]
#B = 20
A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
B = 30
print(solve(A,B))
