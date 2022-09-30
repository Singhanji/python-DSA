import sys

def bar(x, y, c):
    if y == 0:
        return 0
    print(f"-----------count: {c}--------")
    print(f"-----------X: {x}--------")
    print(f"-----------Y: {y}--------")    
    print(x + bar(x, y-1, c))
    
    if c == 1:
        sys.exit()
    c += 1
    return (x + bar(x, y-1, c))

    


def foo(x,y):
    c = 0
    if y == 0:
        return 1    
    return bar(x, foo(x, y-1), c)

print(foo(3, 5))