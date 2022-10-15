# Given Unsorted array[N] distinct elements, return any local minima. 
# An element is said to be local minima, if it is less than it's adjacent elements.
# SC: O(N), SC: O(1)

def solve(A):
    n = len(A)
    ans = []
    if A[0] < A[1]:
        ans.append(A[0])
    if A[n-1] < A[n-2]:
        ans.append(A[n-1])

    for i in range(1,n-1):
        if A[i] < A[i-1] and A[i] < A[i+1]:
            ans.append(A[i])
    return ans
        
A = [9, 8, 7, 3, 6, 4, 1, 5, 2]
print(solve(A))
