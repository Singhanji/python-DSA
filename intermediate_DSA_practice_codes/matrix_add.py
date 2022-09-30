from regex import R
def inp(r, c):
    mat = [[int(input()) for x in range(c)] for y in range(r)]

    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = ' ')
        print()



class Matrix():
    r = 0
    c = 0


    def __init__(self, r, c) -> None:
        self.rows = r
        self.columns = c

    def input(self, a, b):
        return inp()

    def add(self, x):
        pass


inp(2, 2)
m1 = Matrix(1, 2)
m1.input()
m1.rows
m1.columns
