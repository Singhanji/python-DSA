def pow(A, B, C):
  return calculateExponent(A,B,C)

def calculateExponent(base,power,mod):
  if power == 0:
    return 1 % mod

  if power == 1:
    return base % mod

  exponent = (calculateExponent(base, power//2, mod)) % mod

  if power % 2 == 0:
    return (exponent * exponent) % mod
  else:
    return ((exponent * exponent) % mod * base ) % mod

A = 64228540
B = 77622773
C = 88392672
print(pow(A,B,C))

