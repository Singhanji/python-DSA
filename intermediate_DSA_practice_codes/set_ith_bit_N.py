# Given N & i, set the ith bit in N.
# N = 10, N = 1010
# i = 2

def setBit(N,i):
    return (N | (1<<i))

N = 23
i = 2
print(setBit(N,i))



