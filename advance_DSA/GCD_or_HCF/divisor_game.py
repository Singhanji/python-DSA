def solve(A,B,C):
    res = []

    if A % B == 0 and A % C == 0:
        return A//B,A//C
            

A = 12
B = 3
C = 2
print(solve(A,B,C))