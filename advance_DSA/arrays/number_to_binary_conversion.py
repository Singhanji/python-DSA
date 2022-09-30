# convert array of decimal numbers to binary numbers

def binary(A):
    n = len(A)
    for i in range(32):
        for j in range(n):
            A[j]