# Tower Of Hanoi


def solve(A):
    ans = []
    
    def TOH(n, start, temp, dest):
    
        if n == 0:
            return
        TOH(n-1, start, dest, temp)
        curr = [n, start, dest]
        ans.append(curr)
        TOH(n-1, temp, start, dest)
        return ans
    
    TOH(A, 1, 2, 3)
    return ans

A = 2
print(solve(A))