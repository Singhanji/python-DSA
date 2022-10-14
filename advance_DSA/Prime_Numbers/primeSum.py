import math


def primeSum(A):
    isPrime = [True for i in range(A+1)]
    isPrime[0] = False
    isPrime[1] = False
    val = int(math.sqrt(A)) + 1
    for i in range(2, val):
        if isPrime[i]:
            for j in range(i*i, A+1, i):
                isPrime[j] = False
        itr = 2
        while True:
            if isPrime[itr] and isPrime[A-itr]:
                return[itr, A-itr]
    itr+=1

A = 4
#A = 6   
print(primeSum(A))