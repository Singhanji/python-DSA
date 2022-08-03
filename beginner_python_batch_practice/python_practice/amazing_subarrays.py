a = input()
n = len(a)
amz = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
c = 0
ans = 0

for i in range(n-1,-1,-1):
    c += 1
    if a[i] in amz:
        ans += c
   
print(ans)
