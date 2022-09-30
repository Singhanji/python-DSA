def rangeSum(A, B):
        n = len(A)
        m = len(B)

        pf = [n+1]
        pf[0] = A[0]

        for i in range(1, n):
            pf[i] = pf[i-1] + A[i-1]

        ans= [m]

        for i in range(m):
            ans[i] = pf[B[i][1]] - pf[B[i][0] - 1]
        return ans

A = [1, 2, 3, 4, 5]
B = [[1, 4], [2, 3]]
print(rangeSum(A, B))