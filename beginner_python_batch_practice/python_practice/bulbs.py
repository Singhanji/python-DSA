a = [0, 1, 0, 1]

n = len(a)
c = 0

for i in range(n):
    if a[i] == 0:
        a[i] = 1
#        c += 1
   elif a[i] == 1:
        a[i] = 0
    c += 1

print(c)
