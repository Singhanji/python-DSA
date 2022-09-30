def flip(A):
        n = len(A)
        print(n)
        c = A.count('1')
        if c == n:
            return []

        a = [0] * n
        for i in range(n):
            if A[i] == '0':
                a[i] = 1
            else:
                a[i] = -1

        maxSum = -float('inf')
        curSum, l, r, currL = 0, 0, 0, 0
        for i in range(n):
            curSum += a[i]
            if curSum < 0:
                curSum = 0
                currL = i + 1
                continue
            if curSum > maxSum:
                maxSum = curSum
                l = currL
                r = i
        l += 1
        r += 1
        return [l,r]

A = '010'
#A = '111'
print(flip(A))