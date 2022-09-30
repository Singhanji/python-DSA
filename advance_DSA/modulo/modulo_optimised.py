# Given A & B, A>B find no. of m > 0 such that A % M = B % M, A = 10, B = 4
# Optimised Approach
# TC: O(A)

def solve(A,B):
    c = []
    m = A-B
    
    for i in range(1,m+1):
        if m % i == 0:
            c.append(i)
    return c


A = 24
B = 12
print(solve(A,B))