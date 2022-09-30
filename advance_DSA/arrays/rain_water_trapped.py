def trap(A):
    n = len(A)
    pf = [0]* n
    pf[0] = A[0]
    lmax = 0
    rmax = 0
    for k,v in enumerate(A):
        print(f'A[k]: {A[k]}')
        print(f'A[k+1]: {A[k+1]}')
        if A[k] > A[k+1]:
            #print("here")
            pf.append(A[k])
            #print(f'pf[k]: {pf[k]}')
        else:
            pf.append(A[k+1])
        
    lmax = pf[k-1]
    return lmax

A = [4, 2, 5, 7, 4, 2, 3, 6, 8, 2, 3]
print(trap(A))
    