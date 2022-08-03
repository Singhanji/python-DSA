n = int(input())
    
temp = n
sum = 0

while temp > 0:
    num = temp % 10
    nc = num ** 3
    sum += nc
    temp //= 10
    
    if n == sum:
        print(n, end=' ')
