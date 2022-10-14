def primeNum(N):

#   prime = [True for i in range(N+1)] 
    prime = [True] * N

    p = 2

    while(p*p <= N):
        if prime[p] == True:
            for i in range(p*p, N, p):
                prime[i] = False
        p += 1
    c = 0
    for i in range(2,N):
        if prime[i] == True:
            print(i, end = ' ')
            

N = 1000
primeNum(N)