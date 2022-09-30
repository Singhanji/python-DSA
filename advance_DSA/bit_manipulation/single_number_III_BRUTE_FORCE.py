# Single Number III : Given arr[N], every element repeats twice except 2 elements find the 2 unique elements ( which occurs 1 time )

def solve(A):
    n = len(A)
    res = []
    ans = []
    for i in range(n):
        c = 0
        list = A[i+1::]
        if A[i] not in list and A[i] not in ans:
            res.append(A[i])
        
        else:

            ans.append(A[i])
            
    return res


A = [3, 6, 4, 4, 3, 8]
print(solve(A))

