# Given N & i, unset the ith bit
# N = 23, N = 10111
# i = 2
# ans = 19

def unsetBit(N,i):
    return (N&(~(1<<i)))

N = 23
i = 2
print(unsetBit(N,i))

