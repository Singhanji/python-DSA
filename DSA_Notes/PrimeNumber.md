# What is Prime Number?
- A number which is divisble by 1 and itself only.
- OR, a number which has only 2 factors.
- Eg: 10 - Not prime
    --> factors of 10: 1, 2, 5, 10
      7  - Prime  
    --> factors of 7: 1, 7

# Check whether a given number is prime or not?
- we can count the factors of N, if it is 2 then the number is prime else not.

Eg: from i = 1 to N, *TC*: O(N), *SC*: O(1)

   //  def Prime(N):
        c = 0  
        i = 2
        while(i < N):
            N % i == 0:
                c += 1
        if c == 2:
            return True
        return False

   //

Eg: from i = 1 to root(N), *TC*: O(root(N)), *SC*: O(1)
    // def Prime(N):
        c = 0
        i = 2
        while(i*i <= N):
            N % i == 0:
                c += 1
            i += 1
        if c == 2:
            return True
        return False
    //

# Print all prime Numbers from 1 to N:
- TC: O(N*N)
- SC: O(1)
    // def printPrime(A):
        for i in range(2,A):

            if A % i == 0:
                return False  
        return True

        A = 10
        for i in range(2,A+1):
            if(printPrime(i)):
                print(i, end = ' ')
    //

# Optimisation of above code using Algo: Seive Of Eratosthenes
- TC: O(N(log(logN)))
- SC: O(N)

    // def allPrimes(N):
        for i in range(N):
            primes = [True] * N
        
        for i in range(2, N):
            if primes[i] == True:
                for j in range(2*i, N, i):
                    primes[j] = False

        for i in range(2, N):
            if primes[i] == True:
                print(i, end = ' ')
    //
    


