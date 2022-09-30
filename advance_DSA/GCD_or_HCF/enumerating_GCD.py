# You are given a number A and a number B. Greatest Common Divisor (GCD) of all numbers between A and B inclusive is taken (GCD(A, A+1, A+2 ... B)). You have to return the value of GCD found.

def gcd(a,b):

    if b == 0:
        return a
    res = gcd(b, a%b)
    return str(res)

def solve(A,B):
    A = int(A)
    B = int(B)
    ans = 0
    array = range(A,B+1)
    for i in array:
        i = int(i)
        ans = gcd(ans,i)
    
A = "1"
B = "3"


print(solve(A,B))