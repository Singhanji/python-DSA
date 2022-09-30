#  Prime Modulo Inverse
# Given two integers A and B. Find the value of A-1(-1 is inverse here i.e 1/A) mod B where B is a prime number and gcd(A, B) = 1.
# A-1 mod B is also known as modular multiplicative inverse of A under modulo B.

import sys
sys.setrecursionlimit(10**6)
def power(a,b,p):
    if b == 0:
        return 1
    c = power(a,b//2,p)
    if b%2 == 0:
        return ((c%p)*(c%p))%p
    else:
        return (((c%p)*(c%p))*a%p)%p   
  


A = 12
B = 55557209
#A = 3
#B = 5
print(power(A,B-2))
