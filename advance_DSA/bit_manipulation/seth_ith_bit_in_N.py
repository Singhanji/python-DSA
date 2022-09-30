# Given N & i, set the ith bit in N

def solve(N, i):
    return N | (1<<i)

A = 23
i = 2
print(solve(A,i))