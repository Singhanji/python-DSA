# Brute Force approach for - Non repeating element in Array
# TC: O(N^2)
# SC: O(1)


def NRE(A):
    n = len(A)
    for i in range(n):
        c = 0
        for j in range(n):
            if A[i] != A[j]:
                c += 1
        return A[i]


# Driver Code

A = [1, 2, 3, 1, 2, 5]
print(NRE(A))
