# Add Binary Strings

"""
A = "100"
B = "11"

n = len(A)
m = len(B)
ans = []

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        s = A[i] + B[j]
        d = s % 2
        c = s // 2
""" 

def addBinary(A, B):
        carry = 0
        i = len(A) - 1
        j = len(B) - 1
        ans = ''

        while(i >= 0 or j >= 0 or carry):
            Sum = 0
            print("SUM:", Sum)
            if (i >= 0):
                Sum += int(A[i])
                i -= 1
            if (j >= 0):
                Sum += int(B[j])
                j -= 1

            Sum += carry
            digit = Sum % 2
            carry = Sum // 2

            ans += str(digit)

        return ans[::-1]


# Driver code
A = "100"
B = "11"
print(addBinary(A,B))
