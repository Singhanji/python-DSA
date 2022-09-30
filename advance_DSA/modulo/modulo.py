# Given A & B, A>B find no. of m > 0 such that A % M = B % M, A = 10, B = 4
# Brute Force Approach
# TC: O(A)

def solve(A,B):
    c = 0
    for m in range(1, A+1):
        if A % m == B % m:
            c += 1
    return c

A = 10
B = 4
print(solve(A,B))
