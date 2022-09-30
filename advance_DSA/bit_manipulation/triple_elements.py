# Given Arr[N] every element repeats thrice except 1, find the unique element
# Optimized approach

def tripletrouble(A):
    ans = 0
    n = len(A)
    for i in range(32):
        c = 0
        for j in range(n):
            if (A[j]>>i) & 1 == True:
                c += 1
        if c % 3 != 0:
            ans = ans + (1<<i)

    return ans


#A = [6, 5, 6, 4, 5, 6, 5]
A = [0,0,0,1]
print(tripletrouble(A))