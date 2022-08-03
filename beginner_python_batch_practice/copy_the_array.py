n = int(input())

A = []
for i in range(n):
    x = int(input())
    A.append(x)
print("Elments is Array A is: ", A)

Arr = []
B = int(input())
j = len(A)
for k in range(j):
    A[k] = A[k] + B
    Arr.append(A[k])
    print(Arr)
     
