def SeivePrime(N):
    p = [0 for i in range(N+1)]
    print(p)
    
    ans = 0
    for i in range(2, N+1):
        print(i)
        if p[i] == 0:
            for j in range(2*i, N+1, i):
                p[j] += 1
    for i in range(2,N+1):
        if p[i] == 2:
            ans += 1
    return ans


N = 12
#N = 8
print(SeivePrime(N))