def add():
    a = [[1, 2],
    [3, 4]]

    b = [[1,2],
    [3, 4]]

    res = [[0,0],
    [0,0]]

    for i in range(len(a)):
        for j in range(len(b)):
            res[i][j] = a[i][j] + b[i][j]
        
    for r in res:
        print(r)

add()


