# Divide two integers without using multiplication, division and mod operator. Return the floor of the result of the division.  
# It is not working for the given i/p as o/p is: 2147483648 Mine is: 2147483647
# 
INT_MAX = (1<<31) - 1
INT_MIN = -(1<<31)

def divide(A, B):
    sign = 1
    n = A
    m = B

    if n < 0 and m > 0 or n > 0 and m < 0:
        sign = -1

    n = abs(A)
    m = abs(B)

    
    res = n >> m-1

    if res >= INT_MAX or res < INT_MIN:
        return INT_MAX
    return sign * res

A = -2147483648
B = -1
print(divide(A,B))



