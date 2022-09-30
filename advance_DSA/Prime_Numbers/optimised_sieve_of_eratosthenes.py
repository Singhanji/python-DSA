# Optimisation in sieve of eratosthenes Prime number

def solve(A):

    prime = [True for i in range(A+1)]


    i = 2
    while(i*i <= A):
        if prime[i] == True:
            for j in range(i*i, A+1, i):
                prime[j] = False
        i += 1

    for i in range(2,A+1):
        if prime[i]:
            print(i, end = ' ')

A = 10
solve(A)
