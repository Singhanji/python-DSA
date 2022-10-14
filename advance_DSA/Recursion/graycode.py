def graycode(N):

    if N == 1:
        b = []
#       b.insert(0, 0)        // insert, append anything is fine
#       b.insert(1, 1)    
        b.append(0)
        b.append(1)
        return b

    sq = graycode(N-1)
    print(sq)
    ans = []
    x = len(sq)
    for i in range( x):
        ans.append(sq[i])
        print(ans)

    for j in range(x-1, -1, -1):
        
        ans.append(1<<(N-1) + sq[j])

    return ans



N = 2
print(graycode(N))