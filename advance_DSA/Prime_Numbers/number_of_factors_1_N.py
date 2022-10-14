# Find number of factors from all 1 to N
# TC: ON(root(N))

def factors(N):
    i = 1
    c = 0
    for i in range(1, N+1):
        j = i
        while(i*i <= i+1):
            if j%i == 0:
                c += 1
                print(j, end = ' ')
        j += 1
N = 10
factors(N)
