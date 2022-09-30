# Single Number III : Given arr[N], every element repeats twice except 2 elements find the 2 unique elements ( which occurs 1 time )

def solve(A):
    freq = {}
    n = len(A)
    res = []
    for i in range(n):
        if A[i] in freq:
            freq[A[i]] += 1
        else:
            freq[A[i]] = 1
    
    for i in range(n):
        if freq[A[i]] == 1:
            res.append(A[i])
    return res

A = [1, 2, 4, 1, 2, 5]
print(solve(A))
