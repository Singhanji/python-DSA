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
        return str(N) + '/' + str(D)
     
    def subtract(self, a):
        # Complete the function
        N = self.numerator*a.denominator - self.denominator*a.numerator
        D = self.denominator*a.denominator
        return str(N) + '/' + str(D)
     
    def multiply(self, a):
        # Complete the function
        N = self.numerator * a.numerator
        D = self.denominator * a.denominator
        return str(N) + '/' + str(D)
    
    
c1 = Fraction(2, 3)
c2 = Fraction(4, 5)
res = c1.add(c2)
print(res)
"""print(c1.numerator,c1.denominator)
print(c2.numerator, c2.denominator)
"""
res1 = c1.subtract(c2)
print(res1)

res2 = c1.multiply(c2)
print(res2)

"""res1 = c1.subtract(c2)
print(res1.numerator, res1.denominator)
res2 = c1.multiply(c2)
print(res2.numerator, res2.denominator)
"""