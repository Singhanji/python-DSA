def printSumOfSubArray(A, start, end):
    sum = 0
    for i in range(start, end+1):
        sum += A[i]
    print(sum, end=' ')

A = [1, 2, 3, 4, 5, 6]
n = len(A)
s = 2
e = n-1
printSumOfSubArray(A,s,e)
