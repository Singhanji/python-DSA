# Given x & y, set x continuous bits & unset y continuos bits
# x = 3
# y = 2
# 11100 ==> 28(ans)

def continuous_bits(x,y):
    n = x+y
    
    for i in range(n-1,-1,-1):
        print(i)
        while(i==x+1):
            return (1<<i)

x = 3
y = 2
print(continuous_bits(x,y))
