n = int(input())


sum = 0
temp = n

for i in range(1,n+1):
    while temp > 0:
        num = temp % 10
        nc = num ** 3
        sum += nc
        num = temp // 10
    
if n == sum:
    print(c, end=' ')
        


