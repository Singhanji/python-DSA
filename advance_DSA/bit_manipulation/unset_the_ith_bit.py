#Given N & i, unset the ith bit

def solve(N, i):
    return N & (~ (1<<i))


N = 23
i = 2
print(solve(N,i))