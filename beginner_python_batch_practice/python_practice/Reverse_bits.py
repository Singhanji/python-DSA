# Reverse the bits of an 32 bit unsigned integer A.

def solve(A):
    res = 0
    while(A>0):
        for i in range(32):
            y = A & 1
            mul = (1 << y)
            res += (y * mul)
            A >>= 1
            print(A,end =' ')
    return res

A = 3
print(solve(A))
