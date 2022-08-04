# Program for min cost to remove all elements
# TC:
# SC:

def solve(A):
    A.sort()
    print(A)
    cost = 0
    n = len(A)

    for i in range(n):
        cost = cost + (i+1) * A[i]
        print('cost: ', cost)
    return cost


A = [3, 5, 1, -3]
print(solve(A))
