def SubArrays(A, start, end):
    for i in range(start, end + 1):
        print(A[i], end=' ')
    print()

def AllSubArrays(A):
    n = len(A)

    for i in range(n):
        for j in range(i,n):
            print(SubArrays(A, i, j))


A = [1, 2, 3, 4, 5, 6]
print(AllSubArrays(A))
