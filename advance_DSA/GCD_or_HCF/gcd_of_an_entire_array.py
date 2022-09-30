# Given an array, calculate gcd of entire array
# TC: O(Nlog2max()), max = max of array

def gcd(a,b):

    if b == 0:
        return a
    return gcd(b, a % b)



def solve(A):
    ans = A[0]
    n = len(A)
   
    for i in range(1,n):
        
        ans = gcd(ans,A[i])
        
    return ans

#A = [6, 12, 15]
A = [8, 16, 12, 10]
print(solve(A))