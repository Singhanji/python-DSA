def subarraySum(A):
    n = len(A)
    c = 0
    ans = 0
    for i in range(n):
        c = (i+1)*(n-i)
        ans += (c * A[i])
    return ans

A = [1, 2, 3]
print(subarraySum(A))
