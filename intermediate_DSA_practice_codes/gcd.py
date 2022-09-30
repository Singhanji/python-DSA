def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)


a = 22
b = 15
print(gcd(a,b))