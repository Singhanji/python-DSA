
def solve(A, B):
    n = len(A)
    c = 0
    flag = 0
    for i in range(n):  
        if A[i] == B:
            flag = 1
        if A[i] > B:
            c += 1
    if flag == 0:
        return -1
    
    
    return c



A = [1, 4, 2]
B = 3
print(solve(A,B))