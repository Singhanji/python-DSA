# Given N and i, check if i bit position is set or not
# N = 28, N = 11100 
# i = 1

def solve(N,i):
#    return ((N>>i)&1)==1 (Right shift method), OR
    return (N&(1<<i)) != 0  # (Left shift method)

N = 28
i = 1 
print(solve(N,i))
