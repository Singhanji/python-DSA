# Count of divisors for an array

from tkinter import N

from check_prime_num import prime


def sieveoferatosthenes(n):
    n = 10**6
    prime = [True] * n
    p = 2
    while(p*p <= n):
        if prime[p] == True:
            for i in range(p*p, n, p):
                prime[i] = False
        p += 1
        c = 0
        for i in range(2, N):
            if prime[i] == True:
                c += 1
        return c
ans = 1
for p in prime:
    if p*p*p > n:
        break
    c = 1
    whi
