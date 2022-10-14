import sys
import faulthandler
sys.setrecursionlimit(10**6)


def fact(N):
    if N == 0 or N == 1:
        return 1
    return (N*fact(N-1)) % 1000003

def findRank(A):
    ans = 0
    n = len(A)
    for i in range(n):
        c = 0
        for j in range(i+1, n):
            print(A[j], '<', A[i])
            if A[j] < A[i]:
                c += 1
                print(c)
        ans += c * fact(n-i-1) 
    return ans + 1 % 1000003
faulthandler.enable()

#A = "acb"
A = 'DTNGJPURFHYEW'
print(findRank(A))