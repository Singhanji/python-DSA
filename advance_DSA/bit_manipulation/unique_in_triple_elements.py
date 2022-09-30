import sys


def solve(A):

    n = len(A)

    threeN = sys.maxsize
    threeNp1 = 0
    threeNp2 = 0
    

    for i in range(n):
        cthreeN = A[i] & threeN
        cthreeNp1 = A[i] & threeNp1
        cthreeNp2 = A[i] & threeNp2

        threeN = threeN & (~cthreeN)
        threeNp1 = cthreeN | threeNp1

        threeNp1 = threeNp1 & (~cthreeNp1)
        threeNp2 = cthreeNp1 | threeNp2

        threeNp2 = threeNp2 & (~cthreeNp2)
        threeN = threeN | cthreeNp2

    return threeN

A = [1, 2, 3, 1, 7, 2, 3, 1, 3, 2]
print(solve(A))



