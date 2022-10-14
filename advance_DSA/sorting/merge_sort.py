def merge(A, s, m, e):
    N = e - s + 1
    B = [0] * N
    n = len(A)
    p1 = s
    p2 = m+1
    p3 = 0

    while(p1 <= m and p2 <= e):
        if A[p1] <= A[p2]:
            B[p3] = A[p1]
            p1 += 1
            p3 += 1
        else:
            B[p3] = A[p2]
            p2 += 1
            p3 += 1
    while(p1 <= m):
        B[p3] = A[p1]
        p1 += 1
        p3 += 1
    while(p2 <= e):
        B[p3] = A[p2]
        p2 += 1
        p3 += 1

    i = s
    j = 0
    while(i <= e):
        A[i] = B[j]
        i += 1
        j += 1
    return A

def mergeSort(A, s, e):
    
    if s == e:
        return

    m = (s+e)//2
    mergeSort(A, s, m)
    mergeSort(A, m+1, e)
    merge(A, s, m, e)
    return A

A = [4, 8, -1, 2, 6, 9, 11, 3, 4, 7, 13, 0]
#A = [3, 10, 6, 15, 8, 12, 2, 18, 17]
s = 0
m = 0
e = len(A)-1
print(mergeSort(A, s, e))

