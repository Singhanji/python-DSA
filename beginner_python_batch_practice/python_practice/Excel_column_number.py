# Given a column title as appears in an Excel sheet, return its corresponding column number.

def titletoNumber(A):
    n = len(A)
    ans = 0
    mul = 1
    for i in range(n-1,-1,-1):
        ans += mul *(ord(A[i])-ord('A')+1)
        mul *= 26
    return ans


A = 'AB'
print(titletoNumber(A))
