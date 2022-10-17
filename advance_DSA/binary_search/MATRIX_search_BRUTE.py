# Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A. This matrix A has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.
# NOTE: Rows are numbered from top to bottom, and columns are from left to right.
# TC: O(N*M), SC: O(1)

def searchMat(A,B):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == B:
                return 1
    return 0


#A = [[1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
#    ]
#B = 3
A = [[5, 17, 100, 111],
    [119, 120, 127, 131],
    ]
B = 3
print(searchMat(A,B))