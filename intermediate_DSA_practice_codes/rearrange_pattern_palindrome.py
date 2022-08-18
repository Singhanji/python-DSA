def palindrome(A):

    l = []
    n = len(A)

    for i in range(n):
        if A[i] in l:
            l.remove(A[i])
        else:
            l.append(A[i])

        if (len(l) == 0 and n & 1 != 1) or (n & 1 == 1 and len(l) == 1):
            return 1
        else:
            return 0


A = "madma"
print(palindrome(A))