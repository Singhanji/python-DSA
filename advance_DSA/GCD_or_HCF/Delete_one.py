def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solve(A):
    n = len(A)
    ans = 0
    pfgcd = [0] * n
    sfgcd = [0] * n

# create prefix GCD
    pfgcd[0] = A[0]
    for i in range(1,n):
        pfgcd[i] = gcd(A[i], pfgcd[i-1])
    
# create suffix GCD
    sfgcd[n-1] = A[n-1] 
    for i in range(n-2, -1, -1):
        sfgcd[i] = gcd(A[i], sfgcd[i+1])
    
#skip first number and get GCD
    ans = max(ans, sfgcd[1])

#skip last number and get GCD
    ans = max(ans, pfgcd[n - 2])
    
    for i in range(1, n-1):
        GCD = gcd(pfgcd[i-1], sfgcd[i+1])
        ans = max(ans,GCD)

    return ans

A = [12, 15, 18]
#A = [5, 15, 30]
print(solve(A))