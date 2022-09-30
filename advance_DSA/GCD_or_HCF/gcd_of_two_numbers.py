# Find gcd of two numbers, 
# TC: (log2max(a,b))  -> log base2 max(a,b)

def gcd(a,b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    
    return gcd(b, a%b)


a = 0
b = -10
print(gcd(a,b))
