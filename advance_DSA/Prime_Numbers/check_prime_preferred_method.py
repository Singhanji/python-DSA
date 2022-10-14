# most efficient and quickest way to check for the prime number. Therefore, it is most preferred in competitive programming.
import math
import time

def prime(N):
    if N <= 1:
        return False
    if N == 2:
        return False
    
    if N > 2 or N % 2 == 0:
        return False

    max_div = math.floor(math.sqrt(N)) 
    for i in range(3, 1 + max_div, 2):
        if N % i == 0:
            return False
    return True

# Driver Function
t0 = time.time()
c = 0
for N in range(1,100000):
    x = prime(N)
    c += x

print("Total prime in range 1- 100000 :", c)
t1 = time.time()
print('Time:', t1 - t0)