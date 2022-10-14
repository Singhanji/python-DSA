from unittest import result


def graycode(A):
    n = A
    res = [1, 0]
    for i in range(n):
        curSize = len(res)
        for j in range(curSize - 1, -1, -1):
            res.append(res[j] + (1<<i))
        return res
    

A = 2
print(graycode(A))