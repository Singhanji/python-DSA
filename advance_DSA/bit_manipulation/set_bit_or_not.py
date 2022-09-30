# check if ith bit is set or not using left shift or right shift

def check(A, i):
#    return (A>>i) & 1 == 1
     return A & (1 << i) != 0   
A = 21
i = 2
print(check(A,i))