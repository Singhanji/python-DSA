from regex import R


class Matrix():
    rows = 0
    columns = 0


    def __init__(self, r, c) -> None:
        self.rows = r
        self.columns = c
        self.mat = [[0 for j in range(c)] for i in range(r)]

    def input(self):
        for i in range(self.rows):
            self.mat[i]=list(map(int, input().split(' ')[:self.columns]))

    def add(self, x):
        res = x[self.rows, self.columns]
        for i in range(self.rows):
            for j in range(self.columns):
                res.mat[i][j] = self.mat[i][j] + x.mat[i][j]
        return res
    
    def subtract(self, x):
        res = x[self.rows, self.columns]
        for i in range(self.rows):
            for j in range(self.columns):
                res.mat[i][j] = self.mat[i][j] - x.mat[i][j]
        return res

    def transpose(self):
        res = self[self.rows, self.columns]
        for i in range(self.rows):
            for j in range(self.columns):
                res.mat[j][i] = self.mat[i][j]
        return res

    def print(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.mat[i][j], end = ' ')
            print()

m1 = Matrix(2, 2)
m1.input()
m2 = Matrix(2, 2)
m2.input()
c1 = Matrix(2, 2)
c1 = m1.add(m2)
c1 = m1.subtract(m2)
c1 = m1.transpose(m2)
m1.print()
m2.print()
