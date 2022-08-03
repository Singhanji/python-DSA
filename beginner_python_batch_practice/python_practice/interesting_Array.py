def solve(A):
    n = len(A)
    print("n:", n)
    c = 0
    for i in range(n):
        print(i)
        if A[i] % 2 == 1:
            c += 1
            print(c)
    if c % 2 == 1:
        return "No"
    else:
        return "Yes"

A = [9,17]
print(solve(A))
