def SumSubArray(A,s,e):
    sum = 0
    B = []
    for i in range(s,e+1):
        sum += A[i]
        B.append(sum)
        if sum > B:
            B = sum
    return B

def maxSubArray(A):
    for i in range(n):
        for j in range(i,n):
            SumSubArray()

# Driver Code
A = [1, 2, 3, 4, -10]
n = len(A)
    
