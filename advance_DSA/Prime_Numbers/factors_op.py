# WRONG O/P

def factors(N):
    fact = [1 for i in range(N+1)]
    for i in range(2,N+1):
        for j in range(i, N+1, i):
            fact[j] = fact[j]+1
    return fact

N = 15
print(factors(N))