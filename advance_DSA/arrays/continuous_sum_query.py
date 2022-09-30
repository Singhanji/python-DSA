def solve(A, B):
    ans = [0] * A
    l = 0
    r = 0
    val = 0
    
    for i in B:
        l = i[0] -1
        r = i[1] -1
        val = i[2] 
        ans[l] += val
        if r+1 < A:
            ans[r+1] -= val
    n = len(ans)
    for i in range(1, n):
        ans[i] += ans[i-1]
        
        #ans += ans
    return ans

A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(solve(A,B))
