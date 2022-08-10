# First repeating element
# TC:
# SC:

#ar = [1, 2, 3, 2]
ar = [ 10, 5, 3, 4, 3, 5, 6 ]
n = len(ar)
freq = {}

for i in range(n):
    if ar[i] in freq:
        freq[ar[i]] += 1
    else:
        freq[ar[i]] = 1


for i in range(n):
    if freq[ar[i]] > 1:
        print(ar[i])
        break
   
   

