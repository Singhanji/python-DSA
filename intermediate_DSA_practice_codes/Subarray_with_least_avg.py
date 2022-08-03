def Solve(A,K):
    least_avg = float('inf')
    n = len(A)
    s = 0
    c = 0

    for i in range(K):
        print("For i value: ", i)
        s += A[i]
        print("s:", s)
        c += 1
        print("c:", c)
        if c == K:
            avg = s//K
            print("avg:", avg)
            print("s", s)
            print("K:", K)
            least_avg = min(least_avg,avg)
            print("least_avg: ", least_avg)
            print("avg: ", avg)
            c = c -K
    idx = abs(K - i)
    print("idx:",idx)
    print("K:", K)
    return idx

A = [ 3, 7, 90, 20, 10, 50, 40 ] 
K = 3
print(Solve(A,K))
