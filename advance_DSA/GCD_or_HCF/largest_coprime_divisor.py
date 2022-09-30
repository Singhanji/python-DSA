# You are given two positive numbers A and B . You need to find the maximum valued integer X such that:
# Give TLE, Brute Force approach
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def cpFact(A,B):
    res = [1]
    for i in range(2,A+1):
        if A%i == 0:
            res.append(i)
    print(res)
    if len(res) == 2:
        return 1
    for i in res:
        if gcd(i,B) == 1 and i != 1:
            return i

A = 2
B = 3
#A = 5
#B = 10
print(cpFact(A,B))
