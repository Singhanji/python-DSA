# Q4. Add Binary Strings

def addBinary(A,B):
    A = int(A)
    B = int(B)
    return A|B

A = "100"
B = "11"
print(addBinary(A,B))