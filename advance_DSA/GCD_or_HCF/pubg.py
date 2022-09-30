def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solve(A):
    n = len(A)
    ans = A[0]
    for i in range(n):
        ans = gcd(ans,A[i])
    return ans

#A = [6, 4]
A = [2, 3, 4]
print(solve(A))