# Print all number from 1 to N
# TC: O(N*N)

def printPrime(A):
    for i in range(2,A):

        if A % i == 0:
            return False  
    return True


A = 10
for i in range(2,A+1):
    if(printPrime(i)):
        
        print(i, end = ' ')