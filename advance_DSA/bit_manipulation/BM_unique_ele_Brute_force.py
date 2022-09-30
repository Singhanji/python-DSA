# Given Arr[N] every element repeats thrice except 1, find the unique element
# Brute Force

def solve(A):
    res = []
    dup = []
    x = sorted(A)
  
    #n = len(x)
    #print(x)
    for k,v in enumerate(x):
        list = x[k+1::]
        if v not in list and v not in dup:
            res.append(v)
        else:
            dup.append(v)
    return res


A = [6, 5, 6, 4, 5, 6, 5]
print(solve(A))
        