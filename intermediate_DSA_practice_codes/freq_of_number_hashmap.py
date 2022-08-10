# Frequency of numbers
# TC: 
# SC: 


ar = [2, 5, 6, 1, 7, 8, 9, 2, 7, 5, 10, 8]
# created an empty dictionary or hashmap
freq = {}  
n = len(ar)

for i in range(n):
    if ar[i] in freq:
        freq[ar[i]] += 1
    else:
        freq[ar[i]] = 1


#Q = input()

#for _ in Q:
query = int(input())
if query in freq:
    print(freq[query])
else:
    print(0)


