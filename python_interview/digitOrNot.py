def solve(A):
    digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in A:
        print(i)
        if i in digit:
            return True
        return False

A = '27anjana'
print(solve(A))



        
