# Number of 1 Bits
# Given an integer N, count how many set bits are there in N (Assume N to be a 32 bit integer)
# N = 10, N = 1010 , there are 2 set bits(1)

def solve(N,i):
    return ((N>>i)&1)==1

def checkBits(N):
    c = 0
    for i in range(32):
        if solve(N,i):
            c += 1
    return c

N = 45
i = 1 
print(checkBits(N))
    


