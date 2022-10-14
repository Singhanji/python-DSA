# Check if number is Prime or Not 
# TC: O(N*N)


def prime(A):
    c = 0
    for i in range(1, A+1):
        if A%i == 0:
            c += 1
    if c == 2:
        return True
    return False


#A = 10
A = 7
print(prime(A))