# Given A[N] elements, n-1 elements are sorted, sort the entire array.

def sortA(A):
    n = len(A)
    ans = 0
    for i in range(n-1,0,-1):
        c = 0
        if A[i] < A[i-1]:
            A[i-1],A[i] = A[i],A[i-1]
            c = 1
            ans += c
    
    return ans


A = [2, 6, 10, 14, 20, 4]
print(sortA(A))