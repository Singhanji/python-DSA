# Delete One
# Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
# Find the maximum value of GCD.

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(A):
    n = len(A)
    pfgcd = [0] * n
    sfgcd = [0] * n
    
    ans = max(sfgcd,pfgcd)
    for i in range(0, n-2):
        ans = gcd(ans,A[i])
    pfgcd[i] = ans

    for i in range(n-1, 0, -1):
        ans = gcd(ans,A[i])
    sfgcd[i] = ans



A = [18, 24, 30, 21]
print(solve(A))



