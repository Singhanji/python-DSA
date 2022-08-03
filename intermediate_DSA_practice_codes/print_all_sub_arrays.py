# Print all sub arrays of a given array

def printSubArray(A,s,e):
    for i in range(s,e+1):
        print(A[i], end = ' ')
    print()

def printAllSubArrayelements(A,s,e):
#    sum = 0
    for i in range(n):
        for j in range(i,n):
            printSubArray(A,i,j)

A = [1, 2, 3, 4, 5, 6]
s = 0
n = len(A)
e = n-1
printAllSubArrayelements(A,s,e)




