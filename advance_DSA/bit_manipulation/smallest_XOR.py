# Smallest XOR

def solve(A,B):
    c = 0
    for i in range(32):
        print(i)
        res = A ^ i
        while(res != 0):
            if (res & 1) >> 1 == 1:
                c += 1
            
            if c == B:
                return res
    

A = 3
B = 3
print(solve(A,B))