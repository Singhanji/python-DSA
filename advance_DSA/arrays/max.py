def maxset(A):
        l = 0
        r = 0

        max_sum = float('-inf')
        cur_sum = 0

        lmax = 0
        rmax = 0
        for i in range(len(A)):
            if A[i] < 0:
                l , r = i+1, i+1
                cur_sum = 0
            else:
                r += 1
                cur_sum += A[i]
           
            if cur_sum > max_sum:
                lmax , rmax = l , r
                max_sum = cur_sum
            elif cur_sum == max_sum:
                curlength = r - l
                maxleng = rmax - lmax
                if curlength > maxleng:
                    lmax , rmax = l , r

        return A[lmax:rmax]

A = [0, 0, -1, 0]
print(maxset(A))