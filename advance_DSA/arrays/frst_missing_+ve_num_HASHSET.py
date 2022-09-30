def solve(A):
    arrHS = set()
    n = len(A)
    for i in range(n):
        arrHS.add(A[i])
    print(arrHS)
    idx = 1
    while(True):
        if idx not in arrHS:
            return idx
        idx += 1
        
#A = [1, 2, 3, 0, 1, 2, 3, 5, 6]
A = [1, 2, 4, 3, -1, -5]
print(solve(A))