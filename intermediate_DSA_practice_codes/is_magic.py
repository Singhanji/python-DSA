import sys
sys.setrecursionlimit(10**6)


def MagicNum(N):
    if N == 0:
        return 0
    
    rem = N%10
    N = N//10
    res = (rem + MagicNum(N))
    
def result():
    MagicNum(res)
    if res == 1:
        return 1
    return 0
N = 83557
print(MagicNum(N))
