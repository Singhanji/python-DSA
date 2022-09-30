def digitSum(N):
    if N == 0:
        return 0
    
    
    
    rem = N%10
#    print('rem', rem)
#    s += rem
#    print('sum', s)
    N //= 10
    return (rem + digitSum(N))

N = 1234
print(digitSum(N))
    
