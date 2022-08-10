# TC = O(nlogn) + O(n) = O(nlogn)
# SC = O(1)


def minCost(A):
    A.sort(reverse=True)   # O(nlogn)
    print(A)
    n = len(A)
    cost = 0
    
    for i in range(n):                
        cost = cost + (i+1)*A[i]
        print('cost ' ,cost, '+', 'i+1 ', i+1, '*', 'A[i] ', A[i])

    return cost


A = [3, 5, 1, -3]
print(minCost(A))
