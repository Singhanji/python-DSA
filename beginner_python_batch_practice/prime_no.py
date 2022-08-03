n = int(input())

# Prime no. is a natural no. which is greater than 1, divisible by 1 & itself.
# Checking if n(user i/p) is greater than 1

if n > 1:

    for x in range(2,n):
        if n % x == 0:
            print("NO")
            break
    else:
        print("YES")
