def subseq(A):
    A.sort()
    n = len(A)
    ans = 0
    for i in range(n):
        ans = ans + A[i] * (1<<i)
    return ans

A = [3, 1, -4]
print(subseq(A))