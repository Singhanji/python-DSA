def solve(A, B):
    ans = A
    print(ans)
    for i in range(B):
        print(i)
        if (A & (1<<i)):
                print(A&(1<<i))
                ans -= (1<<i)
                print('ans:', ans)
    return ans

A = 25
B = 3
print(solve(A,B))


# OR simply
# return (A & ~(2**B-1))

