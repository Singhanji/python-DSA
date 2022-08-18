# K occurances: 
# TC:
# SC:

def getSum(A, B, C):
    freq = {}
    s = set()

    for i in range(A):
        if C[i] in freq:
            freq[C[i]] += 1
        else:
            freq[C[i]] = 1

    for i in freq:
        if freq[C[i]] == B:
            s.add(C[i])
    if len(s) > 0:
        print(s)
        return sum(s)
        
    return -1



A = 5
B = 2
C = [1, 2, 2, 3, 3]
print(getSum(A,B,C))


