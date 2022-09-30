n = int(input())
s = 0
for i in range(n):
    while(n != 0):
        rem = n % 10
        rem_cube = rem*rem*rem
        s += rem
        n = n//10
    if s == n:
        print(n)