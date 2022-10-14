# Brute Forec Approach
# TC: N*N*root(N)


def isPrime(N):
    c = 0
    for i in range(1, N+1):
        if N%i == 0:
            c += 1
    if c == 2:
        return True
    return False

def solve(A):
    ans = 0
    for i in range(1, A+1):
        c = 0

        for j in range(1, A+1):
            if i%j == 0 and isPrime(j):
                c += 1
            
        if c == 2:
            ans += 1
    return ans
        
A = 8
print(solve(A))


