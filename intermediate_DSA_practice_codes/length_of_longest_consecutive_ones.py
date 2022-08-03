# Givien a binary   string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.

def Solve(A):
    n = len(A)
    c = 0
    for i in range(n):
        if A[i] == 1:
            c += 1
        if c == n:
            return n
    ans = 0
#    L = 0
#    R = 0

    for k, v in enumerate(A):
        
        if v == '1':
            continue
        else:
            L = 0
            R = 0
            s = k-1
            while s >= 0 and A[s] == '1':
                L += 1
                s -= 1
            s = k+1
            while s < n and A[s] == '1':
                R += 1
                s += 1
        if L + R == c:
            ones = L+R
        else:
            ones = L+R+1
                       
        ans = max(ans,ones)

    return ans
    
   

# Driver code

#A = [1, 1, 1, 0, 1, 1, 1, 0, 1]
A = [1,1,1,0,0,0]
print(Solve(A))
