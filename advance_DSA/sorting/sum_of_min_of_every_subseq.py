def subseq(A):
    A.sort()
    n = len(A)
    ans = 0
    for i in range(n):
        ans = ans + A[i] * (1<<n-i-1)
    return ans

#A = [3, 1, -4]
A = [3, 5, 3]
print(subseq(A))