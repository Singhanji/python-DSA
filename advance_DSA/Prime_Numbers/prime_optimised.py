# Check Prime Number
# TC = O(root(N))

def prime(A):
    c = 0
    for i in range(1,A+1):
        if A % i*i == 0:
            c += 1
    if c == 2:
        return True

    return False

A = 2
print(prime(A))  