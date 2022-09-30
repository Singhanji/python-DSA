def pfSum(A, start=1, end=1):
    n = len(A)
    pf = [0] * n
    pf[0] = A[0]
    for i in range(1, n):
        if pf[i-1] > A[i]:
            pf[i] += pf[i-1]
        else:
            pf[i] += A[i]

def sfSum(A):
    n = len(A)
    sf = [0]*n
    sf[n-1] = A[n-1]
    for i in range(n-2, -1, -1):
        if A[i] > A[i+1]:
            print(sf[i])
            sf[i] += A[i]
        else:
            sf[i] += A[i+1]

def trap(A):
    ans = 0
    n = len(A)
    pfSum()
    

    
    for i in range(n-1):
        lmax = max(pf)
    
    return pf, sf




#A = [1, -6, 3, 2, 8, 7]
#A = [4, 8, -1, 6, 3]
A = [3, 10, 6, 7, 0, 2, -1]
print(trap(A))


