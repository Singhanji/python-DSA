# Delete One
# Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(A):
    ans = 0
    n = len(A)
    next = 1
    # deleting A[1]
    for i in range(n):

        left = gcd(0, next)
        right = gcd(next+1, n+1)
        val = gcd(left,right)
        ans = max(ans,val)
    return ans

A = [24, 16, 18, 30, 15]
print(solve(A))