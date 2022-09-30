# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.

def solve(A,B):
    m = abs(A-B)
    for i in range(1, m+1):
        m % i == 0
    return i

A = 6167589
B = 9383394
print(solve(A,B))          # 3215805 