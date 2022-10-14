import sys
sys.setrecursionlimit(10**6)

c = 0
def merge(A, s, m, e):
    p1, p2, p3 = s, m+1, 0
    C = [0 for i in range(e-s+1)]

    while(p1 <= s and p2 <= e):
        if A[p1] <= A[p2]:
            C[p3] = A[p1]
            p3 += 1
            p1 += 1
        else:
            c += m-p1+1
            C[p3] = A[p2]
            p3 += 1
            p2 += 1
            
    while(p1 <= m):
        C[p3] = A[p1]
        p1 += 1
        p3 += 1
    while(p2 <= e):
        C[p3] = A[p2]
        p2 += 1
        p3 += 1
    for i in range(s, e+1):
        A[i] = C[i-1]
    return c
def mergeSort(A, s, e):
    s = 0
    e = len(A) - 1
    
    if s == e:
        return

    m = (s+e)//2
    x = mergeSort(A, s, m)

    y = mergeSort(A, m+1, e)
    z = merge(A, s, m, e)
    return x+y+z


def solve(A):
    mod = 1000000007
    s = 0
    e = len(A) - 1
    res = mergeSort(A, s, e)
    return res % mod
        
A = [3, 2, 1]
print(solve(A))
