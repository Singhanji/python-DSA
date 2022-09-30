# Given Arr[N] every element repeats thrice except 1, find the unique element
# Optimised using HAshMap

def unique(A):
    hmap = {}
    n = len(A)
    for i in range(n):
        if A[i] in hmap:
            hmap[A[i]] += 1
        else:
            hmap[A[i]] = 1

    for i in range(n):
        if hmap[A[i]] == 1:
            return A[i]
        

A = [6, 5, 6, 4, 5, 6, 5]
print(unique(A))
