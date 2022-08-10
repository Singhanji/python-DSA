def longestPalindrome(A):
    
    n = len(A)
    ans = A[0]
        
    def lps(p1, p2):
        while p1 >= 0 and p2 < n and A[p1] == A[p2]:
            p1 -= 1
            p2 += 1

#            r = p2 - p1 - 1
    return A[p1+1:p2]

    res = ''
    for i in range(len(A)):
        t = lps(i,i)
        if len(t) > len(res):
            res = t

        t = lps(i, i+1)
        if len(t) > len(res):
            res = t
        return res


A = "abba"
print(lps(A))