def maxSubArray(A):
    
    n = len(A)
    maxVal = -float('inf')
    curSum = 0
    for i in range(n):
        curSum += A[i]
        maxVal = max(maxVal,curSum)
        if curSum < 0:
            curSum = 0
    return maxVal
#A = [1, 2, 3, 4, -10]
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(A))