# Selection Sort
# Given ar[N] elements, find kth smallest element (return ar[k-1] index element, when array is sorted.)
# Idea 1: Brute force- Sort the array and get k-1th element 
#TC: O(NlogN)


def solve(A, k):
    A.sort()
    
    return A[k-1]

A = [2, 8, 4, -1, 6, 7, 5, 10, -1]
k = 7

print(solve(A, k))