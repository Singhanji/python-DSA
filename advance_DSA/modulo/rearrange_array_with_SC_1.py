# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
def solve(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i] * n
    
    for i in range(n):
        A[i] += A[A[i]//n]//n

    for i in range(n):
        A[i] = A[i] % n

    return A

A = [1, 0]
print(solve(A))
