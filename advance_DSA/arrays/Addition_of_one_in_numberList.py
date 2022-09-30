# Addition of number 1
#WORKING CORRECTLY
    # @param A : list of integers

    # @return a list of integers

def plusOne(A): 

    f=0
    A1=[]
    for i in A:
        if i!=0:
            f=1
        if f==1:
            A1.append(i)

    A1.reverse()
    n = len(A1)
    d=1
    for i in range(n):
        if A1[i]+d>9:
            A1[i]=0
            d=1
        else:
            A1[i]=A1[i]+d
            d=0

    if d ==1:
        A1.append(1)
    A1.reverse()

    return A1


A = [2, 5, 6, 8, 6, 1, 2, 4, 5]
print(plusOne(A))
