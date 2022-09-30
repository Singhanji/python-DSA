# Given a, n, p. Compute a^n %p.

from regex import P


def solve(A, p, n):
    ans = 1
    
    for _ in range(1, n+1):
        ans = (ans * A) % p
    return ans%p


A = 3
p = 7
n = 4

print(solve(A, p, n))

    
