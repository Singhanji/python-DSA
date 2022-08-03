# Given x & y, set x bit and y bit in value 0.

def setBit(x,y):
    return (1<<x) | (1<<y)
    

x = 5
y = 2
print(setBit(x,y))
