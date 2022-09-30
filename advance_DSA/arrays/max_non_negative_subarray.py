# Max non negative SubArray

def maxset(A):
    curSum, maxSum = 0,0
    start,end,s = 0,0,0
    length = 0
    ans = []
    for i in range(len(A)):
        if A[i]<0:
            curSum = 0
            s = i+1
        else:
            curSum+= A[i]
            if curSum > maxSum:
                maxSum = curSum
                start = s
                end = i+1
                length = i - s
            elif curSum == maxSum and i - s > length:
                start = s
                end = i+1
        for i in range(start,end):
            ans.append(A[i])
        return ans


#A = [1, 2, 5, -7, 2, 3]
A = [10, -1, 2, 3, -4, 100]
print(maxset(A))