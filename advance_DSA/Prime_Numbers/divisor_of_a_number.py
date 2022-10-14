# Count no. of divisors in N
# TC: O(root(N)) 


def CntDivisors(N):
    c = 0
    i = 1
    while(i*i <= N):
        if N % i == 0:
            if N / i == i:
                c += 1
            else:
                c += 2
        i += 1
    return c

#N = 100
N = 18
print(CntDivisors(N))