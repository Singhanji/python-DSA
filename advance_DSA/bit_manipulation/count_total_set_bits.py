# Given a positive integer A, the task is to count the total number of set bits in the binary representation of all the numbers from 1 to A.

def solve(A):
    ret = 0
    for i in range(1,A+1):
        while i != 0:
            if i & 1:
                ret += 1
            i = i >> 1

    return ret % 1000000007

A = 1000000000
print(solve(A))