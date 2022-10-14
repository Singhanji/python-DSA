def fact(N):
    if N <= 1:
        return 1
    return N * fact(N-1)

def pow(A, B, C):
    
    result = 1
    base = A % C
    while(B > 0):
        if B & 1 == 1:
            result = (result * base) % C
        B = B >> 1
        base = (base * base) % C
    return result % C
def solve(A, B):
    factB = fact(B)
    C = 10**9+7
    p = pow(A, factB, C)
    return p


A = 1
B = 1
print(solve(A,B))