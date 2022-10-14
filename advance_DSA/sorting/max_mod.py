# MaxMod- BruteForce Approach
# TC: O(N*N), SC: O(1)


def solve(A):
    n = len(A)
    max_v = 0
    for i in range(0, n-1):
        
        for j in range(0, n-1):
            if max_v < A[i] % A[j]:
                max_v = A[i] % A[j]
    return max_v

A = [1, 2, 44, 3]
print(solve(A))
