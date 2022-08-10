# Noble Integer: When no. of elements are duplicates.
# TC: O(nlogn)
# SC: O(1)

def NobleDupInt(A):
    n = len(A)
    c = 0
    ans = 0
    for i in range(n):
        if A[i] != A[i-1]:
            c = i
        if c == A[i]:
            ans += 1
    return ans



#A = [-3, 0, 2, 2, 5, 5, 5, 5, 8, 8, 10, 10, 10, 14]
#A = [3, 2, 1, 3]
#A = [1, 1, 3, 3]
A = [5, 6, 2]
print(NobleDupInt(A))
