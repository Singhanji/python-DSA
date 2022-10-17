# Matrix Search
# TC: O(log(N*M)), SC: O(1)

def searchMatrix(A, B):
    rows = len(A)
#    print(rows)
#    print(A)
    cols = len(A[0])
#    print(cols)
#    print(A[0])

    low, high = 0, (rows*cols) - 1

    while(low <= high):
        mid = (low + high) // 2
        i = mid // cols
        j = mid % cols
        if A[i][j] == B:
            return 1
        elif A[i][j] < B:
            low = mid + 1
        else:
            high = mid - 1
    return 0
A = [[1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50],
    ]
B = 3
print(searchMatrix(A,B))