A = [1,2,2,3,1]
n = len(A)
ans = 0
for i in range(n):
    ans = ans ^ A[i]
    print("A:", ans)
    print("A[i]", A[i])
print(ans)
