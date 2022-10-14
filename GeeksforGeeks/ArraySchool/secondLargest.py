def secondLargest(A):
    n = len(A)
    if n < 2:
        return -1
        
    first = -float('inf')
    sec = -float('inf')
    for i in range(n):
        if A[i] > first:
            sec = first
            first = A[i]
        elif A[i] > sec and A[i] != first:
            sec = A[i]
    if sec ==  -float('inf'):
        return -1

    return sec

A = [12, 35, 1, 10, 34, 1]
print(secondLargest(A))