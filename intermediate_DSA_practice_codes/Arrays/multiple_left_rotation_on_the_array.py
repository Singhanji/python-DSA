
"""def swap(A, B_v):
    print(f"B_v: {B_v}")
    B1 = A[0:B_v]
    print(B1)
    B2 = A[B_v::]
    print(B2)
    return B2 + B1 
    

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = [2, 3]
    m = []
    for i in B:
        r = swap(A, i)
        m.append(r)
    print(m)"""


def swap(A, B_v):
    B1 = A[0:B_v]
    B2 = A[B_v::]
    return B2 + B1 

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(A, B):
        m = []
        for i in B:
            r = swap(A, i)
            m.append(r)
        return m

A = [1, 2, 3, 4, 5]
B = [2, 3]
s = Solution
print(s.solve(A,B))