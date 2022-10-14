# Count of divisors
# Brute Force

def COD(A):
    n = len(A)
    res = []
    for i in A:
        s = 1
        c = 0
        while(s <= i):
            if i % s == 0:
                c += 1
            s += 1
        res.append(c)
    return res

A = [2, 3, 4, 5]
print(COD(A))