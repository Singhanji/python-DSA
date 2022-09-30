import sys
sys.setrecursionlimit(10**6)
def palindrome(A,start,end):
    if start>=end:
        return 1
    if A[start]==A[end]:
        return palindrome(A,start+1,end-1)
    return 0

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        start=0
        end=len(A)-1
        return palindrome(A,start,end)



A = "naman"
print(solve(A))




    