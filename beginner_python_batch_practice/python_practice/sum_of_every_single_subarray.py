# Print Sum of Every single sub Array

def SumOfSubArr(A,s,e):
    sum = 0
    for i in range(s,e+1):
        sum += A[i]
    return sum
    print()

def evry_single_sub_arr(A):
    n = len(A)
    for i in range(n):
        for j in range(i,n):
            sum = SumOfSubArr(A,i,j)
            print(sum)


A = [3, -2, 4]
evry_single_sub_arr(A)

