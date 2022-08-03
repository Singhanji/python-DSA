# Given array of N elements, find max subarray sum of length=k (N >= k).

def solve(n,k):
    ans = float('-inf')
    Sum = 0
    s = 0
    e = k-1
    while(e<n):
        for i in range(A[:s:e:]):
            Sum += A[i]
            ans = max(ans,Sum)
            s += 1
            e += 1
        return ans


# Driver code

A = [-3, 4, -2, 5, 3, -2, 8, 2, -1, 4]
n = len(A)
k = 5
print(solve(n,k))

