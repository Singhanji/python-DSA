def solve(A):
    l = list(A)
    print(type(l))
    n = len(l)
    s = 0
    e = n-1
    while(s<e):
        l[s],l[e] = l[e],l[s]
        s += 1
        e -= 1
    return l

A = (10, 1, 1)
print(type(A))
print(solve(A))