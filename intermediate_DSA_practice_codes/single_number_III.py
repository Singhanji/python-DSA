def solve(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans = ans ^ A[i]
    return ans

# Driver Code

A = [1,2,3,1,2,4]
print(solve(A))
