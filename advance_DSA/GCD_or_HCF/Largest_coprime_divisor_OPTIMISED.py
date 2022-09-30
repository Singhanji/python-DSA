def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def cpFact(A,B):
    while(gcd(A,B) != 1):
        A = A // gcd(A,B)
    A = int(A)
    return A


A = 3072364587912
B = 127423659254876
print(cpFact(A,B))
