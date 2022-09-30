def solve(A):
    n = len(A)
    max_v = -float('inf')
    min_v = float('inf')
    for i in range(n):
        if A[i] & 1 != 1 and A[i] > max_v:
            max_v = A[i]
        elif A[i] & 1 == 1 and A[i] < min_v:
            min_v = A[i]
    
    res = max_v - min_v
    return res

#A = [0, 2, 9]
#A = [5, 17, 100, 1]
A = [ -98, 54, -52, 15, 23, -97, 12, -64, 52, 85 ]
print(solve(A))

    