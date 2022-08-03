def solve(A):        
        n = len(A)
        c = 0
        for i in range(n):
            if A[i] == 1:
                c += 1
        
        if c == n:
            return n
        else:
            ans = 0
            for i in range(n):
                L = 0
                R = 0
                if A[i] == 0:
                    for j in range(i-1,-1,-1):
                        if A[j] == 1:
                            L += 1
                        else:
                            break
                    
                    for j in range(i+1,n):
                        if A[j] == 1:
                            R += 1
                        else:
                            break

                if L + R == c:
                    ones = L + R
                else:
                    ones = L + R + 1
                ans = max(ans,ones)
            return ans

# Driver Code

#A = [1,1,1,0,1,1,1,0,1]
A = [1,1,1,0,0,0]
#A = [1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0]
#A = "111000"
print(solve(A))
