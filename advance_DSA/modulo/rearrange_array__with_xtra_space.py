# Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
# With extra space

def solve(A):
    res = []
    n = len(A)
    for i in range(n):
        res.append(A[A[i]])
    print(A)
    return res
    

A = [1, 2, 3, 0]
print(solve(A))
