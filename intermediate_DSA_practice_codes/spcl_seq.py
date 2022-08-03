a = input()
n = len(a)
c = 0

for i in range(n):
    if a[i]=='a':
        for j in range(1,n):
            if a[j]=='g':
                c += 1
print(c)

