# Comman Elements
# TC: 
# SC: 

def solve(A,B):
    
    freqA = {}
    C = []
    
#inserting all elements of A in a map
    for x in A:
        try:
            freqA[x]+=1
        except:
            freqA[x] = 1

    for i in range(len(B)):
        if B[i] in freqA:
            if freqA[B[i]] >=1:
                C.append(B[i])
                freqA[B[i]] -=1
       
    return C

#A = [1, 2, 2, 1]
#B = [2, 3, 1, 2]
A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]

print(solve(A,B))
