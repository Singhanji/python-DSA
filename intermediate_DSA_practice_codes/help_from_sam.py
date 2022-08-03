# Alex and Sam are good friends. Alex is doing a lot of programming these days. He has set a target score of A for himself.
#Initially, Alex's score was zero. Alex can double his score by doing a question, or Alex can seek help from Sam for doing questions,
#that will contribute 1 to Alex's score. Alex wants his score to be precisely A. Also, he does not want to take much help from Sam.

#Find and return the minimum number of times Alex needs to take help from Sam to achieve a score of A.
'''
def solve(A):
    c = 0
    rem = 0
    while(A != 0):
        rem = A % 2
        if rem == 1:
            c += 1
        A = A//2
        print('A: ', A)
    return c

# Driver code
A = 5
print(solve(A))

'''

def solve(A):
    c = 0
    while(A):
        if (A&1 == 1):
            c += 1
        A >> 1
        print(A)
    return c


A = 5
print(solve(A))

