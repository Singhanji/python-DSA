# Print all the prime numbers usimg Sieve of Eratosthenes
# TC : n*(log(logn))

def prime(A):
    p = [True] * A
    p[0] = False
    p[1] = False

    for i in range(2,A):
        if p[i] == True:
            for j in range(2*i,A,i):
                p[j] = False
                
    for i in range(1,A):
        if p[i] == True:
            print(i, end = ' ')

A = 10
prime(A)
