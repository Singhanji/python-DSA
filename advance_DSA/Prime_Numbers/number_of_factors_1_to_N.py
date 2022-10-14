# Wrong O/p ``

def Allfactors(N):

    fact = [1 for i in range(N+1)]

    for i in range(2, N):
        for j in range(i, N, i):
            fact[j] = fact[j] + 1
    return fact

N = 10
print(Allfactors(N))