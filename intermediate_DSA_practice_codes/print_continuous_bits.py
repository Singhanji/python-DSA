def solve(x):
    ans = 0
    while(x>0):
        ans += (1<<x)
        print('ans:', ans)
        x -= 1
        print(x)
    return ans


x = 3
print(solve(x))
