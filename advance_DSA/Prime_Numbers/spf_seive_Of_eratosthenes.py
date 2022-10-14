# Prime Factorisation using Sieve

def primeFactor(n):
    spf = [0 for i in range(n+1)]
    for i in range(2,n+1):
        spf[i] = i

    for i in range(2,n+1):
        if spf[i] == i:
            for j in range(i*i, n+1, i):
                if spf[j] == j:
                    spf[j] = i

    while(n != 1):
        print(spf[n])
        n = n//spf[n]


n = 42
primeFactor(n)