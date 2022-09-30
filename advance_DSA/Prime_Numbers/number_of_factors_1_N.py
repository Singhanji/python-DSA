# Find number of factors from all 1 to N
# TC: ON(root(N))

def factors(N):
    for i in range(1,N+1):
        j = i
        c = 0
        while(i*i <= N):
            if j % i == 0:
                c += 1
                print(i, end = ' ')
            i += 1  
N = 10
factors(N)
