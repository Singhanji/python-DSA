# Observation: A%B will be maximum if A<B and A & B are maximum possible, so here the ans will be the second largest value of the array.
# MaxMod- Optimized Approach
# TC: O(N), SC: O(1)

def maxMod(A):
    n = len(A)
    first = -float('inf')
    sec = -float('inf')

    for i in range(n):
        if first < A[i]:
            sec = first
            first = A[i]

    for i in range(n):
        if sec < A[i] and sec != first and first != A[i]:
            sec = A[i]

    if sec != -float('inf'):
        return sec
    return 0

A = [927, 707, 374, 394, 279, 799, 878, 937, 431, 112]
print(maxMod(A))