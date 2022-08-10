# Nobel Integer - Optimized solution , When there are unique elements in the array.
# TC : O(nlogn), (better than previous soln that gave O(n^2))
# SC : O(n)

def NobleInt(A):
    n = len(A)
    ans = 0
    for i in range(n):
        if A[i] == i:
            ans += 1
    return ans


A = [-10, -5, 1, 3, 4, 5, 10]

print(NobleInt(A))
            

