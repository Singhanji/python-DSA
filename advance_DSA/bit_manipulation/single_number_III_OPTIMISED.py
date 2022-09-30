# Single Number III : Given arr[N], every element repeats twice except 2 elements find the 2 unique elements ( which occurs 1 time )


def solve(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans = ans ^ A[i]
        print(ans)
    pos = 0
    for j in range(32):
        if ans & (1 << j) != 0:
            pos = j
            break

    set = 0
    unset = 0
    for i in range(n):
        if A[i] & (1 << pos) != 0:
            set = set ^ A[i]
        else:
            unset = unset ^ A[i]
    
    if set > unset:
        return unset,set


    return set,unset

#A = [1,2,3,1,2,4]
#A = [ 2308, 1447, 1918, 1391, 2308, 216, 1391, 410, 1021, 537, 1825, 1021, 1729, 669, 216, 1825, 537, 1995, 805, 410, 805, 602, 1918, 1447, 90, 1995, 90, 1540, 1161, 1540, 2160, 1235, 1161, 602, 880, 2160, 1235, 669 ]
#A = [ 186, 256, 102, 377, 186, 377 ]
A = [ 408, 478, 74, 624, 74, 204, 705, 624, 337, 408, 478, 204 ]


print(solve(A))

    
            

