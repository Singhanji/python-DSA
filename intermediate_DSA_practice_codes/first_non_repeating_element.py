# First non repearing element
# TC: 
# SC: 

ar = [1, 2, 3, 1, 2, 5]

n = len(ar)
freq = {}

for i in range(n):
    if ar[i] in freq:
        freq[ar[i]] += 1
    else:
        freq[ar[i]] = 1

for i in range(n):
    if freq[ar[i]] == 1:
        print([ar[i]])
        break



