def maxSubArray(A):
    cur_sum = 0
    max_sum = float('-inf')
    n = len(A)
    for i in range(n):
        cur_sum += A[i]
        max_sum = max(max_sum,cur_sum)
        if (cur_sum < 0):
            cur_sum = 0
    return max_sum

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(A))
