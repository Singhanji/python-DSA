# Factorial from 1 to N
# Brute Force Method
# TC: O(N(root(N)))


def factorial(N):
    res = []
    n = len(N)
    for i in N:
        
        c = 0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
#                res.append(j)

#    print(res)
    
        res.append(c)
    return res

N = [2, 3, 4, 5]
print(factorial(N))


"""

def factN(N):
    res = []
    for i in range(1,N+1):
        j = 1
        while(j <= i+1):
            if i % j == 0:
                res.append[j]
            j += 1
    print(res)

N = 10
factN(N)
"""