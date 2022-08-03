a = [15, -1, 7, 2, 5, 4, 2, 3]
n = len(a)
print(n)
c = 1

for i in range(n-1):
    print(i,end =" ")
    max_val = a[i+1]
    print("max_val:", max_val)
    for j in range(1,n):
        if a[j] > max_val:
            max_val = a[j]
            print("MAX_VAL", max_val)

    if a[i] > max_val:
        print("a[i]>MAX_VAL",a[i])
        c += 1
print(c)
