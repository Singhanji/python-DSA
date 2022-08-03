# Given a, n, p. Compute a^n %p.
# Time complexity = O(n)
# Space complexity = O(1)
# We can optimize it.
# Assuming no overflow

def solve(a,n,p):
    ans = 1
    for i in range(1,n+1):
        ans = ans * a
    return ans % p


a = 3
n = 4
p = 7
print(solve(a,n,p))
