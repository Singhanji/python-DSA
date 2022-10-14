def solve(A,B):
    if B == 0 or len(A) == 0:
        return 0
    
    A.sort()
    ans = float('inf')
    for i in range(len(A)-B+1):
        ans = min(ans, A[i+B-1] - A[i])
    return ans


A = [3, 4, 1, 9, 56, 7, 9, 12]
B = 5
print(solve(A,B))