# Noble Integers

def NobleInt(A):
    A.sort()
    n = len(A)
    c = 0
    for i in range(n):
        c += 1
        p = c - i
        if c == p:
            return 1
        else:
            return -1


A = [6,7,5]
print(NobleInt(A))
