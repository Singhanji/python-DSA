# Every element repeats twice except 1, find unique element

def uniq(A):
    n = len(A)
    A.sort()
    ans = 0
    for i in range(n):
        ans = ans ^ A[i]
        
    return A[i]

A = [3, 2, 3, 7, 2, 8, 7]
print(uniq(A))
