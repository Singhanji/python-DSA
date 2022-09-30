# Implement pow(A, B) % C. In other words, given A, B and C, Find (AB % C).
# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.

def pow(A, B, C):
    result = 1
    base = A % C
    print(f'baseUP: {base}')
    while B > 0:
        print('B', B)
        if B % 2 == 1:
            result = (result*base) % C
            print(f'result: {result}')
        B = B >> 1
        print(f'B: {B}')
        base = (base*base)%C
        print(f'base: {base}')
    return result%C

A = 3
B = 4
C = 7
print(pow(A,B,C))

