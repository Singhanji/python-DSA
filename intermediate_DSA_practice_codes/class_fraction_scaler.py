def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)

class Fraction:
    numerator = 0
    denominator = 0

    # Define constructor here
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def add(self, a):
        # Complete the function
        N = self.numerator*a.denominator + self.denominator*a.numerator
        D = self.denominator*a.denominator
        temp = gcd(abs(N), abs(D))
        N //= temp
        D //= temp
        return Fraction(N,D)
        
    def subtract(self, a):
        # Complete the function
        N = self.numerator*a.denominator - self.denominator*a.numerator
        D = self.denominator*a.denominator
        temp = gcd(abs(N), abs(D))
        N //= temp
        D //= temp
        return Fraction(N,D)

    def multiply(self, a):
        # Complete the function
        N = self.numerator * a.numerator
        D = self.denominator * a.denominator
        temp = gcd(abs(N), abs(D))
        N //= temp
        D //= temp
        return Fraction(N,D)

