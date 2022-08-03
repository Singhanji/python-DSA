# Given an array B of length A with elements 1 or 0. Find the number of subarrays with bitwise OR 1.


# 1. Do xor of all elements. ==> you will get xor_value = 110 i.e. 6 in decimal.

# 2. find the leftmost set bit(i.e. left most '1' value) of xor_value you will get bit_position as 1th place. (Note I started bit positioning from 0th place).

# 3. Do Xor of elements separately whose 1th place bit is Set and whose 1th place bit is UnSet. Your will get unique_number1 as 3 and unique_number2 as 5

# 4. store those separated unique two xor values in result array in ascending order and return the array.

def solve(A,B):
    n = len(B)
    t = A *(A+1)//2
    c,Sum = 0,0
    for i in range(n):
        if B[i]==0:
            c+=1
        else:
            Sum += c*(c+1)//2
            c = 0
            if c>=1:
                Sum += c*(c+1)//2
    return t-Sum


A = 3
B = [1,0,1]
print(solve(A,B))

