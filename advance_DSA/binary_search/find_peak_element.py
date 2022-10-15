def solve(A):
    n = len(A)
    l = 1
    h = n-2

    if A[0] > A[1]:
        return A[0]
    if A[n-1] > A[n-2]:
        return A[n-1]

    while(l<=h):
        m = (l+h)//2
        if(A[m] > A[m+1] and A[m] > A[m-1]):
            return A[m]
        if(A[m] < A[m-1]):
            h = m-1
        else:
            l = m+1
    return A[m]
#A=[1, 2, 3, 4, 5]
#A = [15, 17, 100, 11]
A = [1, 1000000000, 1000000000]
print(solve(A))