"""A = [1, 2, 3, 4, 5]

n = len(A)
sum = 0

for i in range(1,n):
    print(A[i], end = ' ')
    sum += A[i]
print()
print("The sum is:", sum, end =' ')
"""

# Print all values of Subarray

def printSubArray(A, start, end):
    for i in range(start, end + 1):
        print(A[i], end=" ")

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
n = len(A)
e = n - 1

printSubArray(A,s,e)
