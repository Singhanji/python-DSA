# Count Divisors of n in O(n^1/3)
def solve(A):
        res = []
        for i in A:
            c = 0
            j = 1
            while(j*j <= i+1):
            
                if i % j == 0:
                    if j == i//j:
                        c += 1
                    else:
                        c += 2
                j += 1
            res.append(c)
        return res


A = [2, 3, 4, 5]
print(solve(A))