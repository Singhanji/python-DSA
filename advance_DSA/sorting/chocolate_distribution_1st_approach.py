# Given an array A of N integers where the i-th element represent the number of chocolates in the i-th packet.

# There are B number of students, the task is to distribute chocolate packets following below conditions:

# 1. Each student gets one packet.
# 2. The difference between the number of chocolates given to any two students is minimum.
# Return the minimum difference (that can be achieved) between the student who gets minimum number of chocolates and the student who gets maximum number of chocolates.

def solve(A, B):
    if B == 0: return 0
    if not A: return 0
    A.sort()
    N = len(A)


    ans = float('inf')


    for i in range(N-B+1):
        diff = A[i+B-1] - A[i]
        ans = min(ans,diff)
       
    return ans


A = [3, 4, 1, 9, 56, 7, 9, 12]
B = 5
print(solve(A,B))