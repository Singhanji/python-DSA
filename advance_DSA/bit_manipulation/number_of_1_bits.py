# Count Number of 1 Bits in any number
# Eg: N = 10 --> 10 = 1010 --> 2(number of 1's are 2)
# We don't need to convert number to Binary as bit manipulation happens in binary only
"""
def solve(A):
    c = 0
    for i in range(32):
        if A & (1 << i) != 0:
            c += 1
    return c

A = 10
print(solve(A))

"""

# solving using right shift approach
def solve(A):
    c = 0
    while (A > 0):
        if A & 1 == 1:
            c += 1
        A >>= 1
    return c

A = 10
print(solve(A))