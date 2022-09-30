def solve(A):
  count = 0
  n = A
  i = 0
  while n > 0:
    if (n & 1) == 1:
      f = ((1 << i) >> 1) * i
      g = (((1 << i) - 1) & A) + 1
      count += f + g
    n >>= 1
    i += 1
  return count % 1000000007

A = 1000000000
print(solve(A))