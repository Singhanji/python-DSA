# Noble Integers

def NobleInt(A):
    A.sort()
    n = len(A)
    ans = 0
    for i in range(n):
        c = 0
        for j in range(n):
            if A[j] < A[i]:
                c += 1
        if A[i] == c:
            ans += 1
    return ans


A = [-10, -5, 1, 3, 4, 5, 10]
print(NobleInt(A))
