# Program to find if the sequence is forming an Arithematic Progression?
# TC: 
# SC: 

def ap(A):

    n = len(A)
    A.sort()

    diff = A[1] - A[0]
    
    for i in range(n-1):
        if A[i+1]-A[i]!=diff:
            return -1
        
    return 1

#A = [3, 5, 1]
A = [2, 4, 1]
print(ap(A))
