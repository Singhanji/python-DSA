class Matrix:
    # Define properties here
    rows = 0
    columns = 0
    
    
    # Define constructor here
    def __init__(self, rw, col):
        self.rows = rw
        self.columns = col

    def input(self):
        # Complete the function
        r = int(input())
        c = int(input())
        mat = [[int(input()) for  x in range(c)] for y in range(r)]    
    
        for i in range(r):
            for j in range(c):
                print(mat[i][j], end = ' ')
        print()
    def add(self, x: "Matrix") -> "Matrix":
        # Complete the function
        res = [0]
        for i in range(len(self.rows)):
            for j in range(len(x)):
                res[i][j] = self[i][j] + x[i][j]
        for r in res:
            print(r)       
        
    def subtract(self, x: "Matrix") -> "Matrix":
        # Complete the function
        res = [0]
        for i in range(len(self)):
            for j in range(len(x)):
                res[i][j] = self[i][j] - x[i][j]
        for r in res:
            print(r)
    
    
    def transpose(self) -> "Matrix":
        # Complete the function
        pass    
    
    def print(self):
        # Complete the function
        pass

m1 = Matrix(2, 3)
m1.input()
m1.add(2)
m1.subtract(2)




# Matrix a = new Matrix(10, 5)  // 10 rows, 5 columns
# a.input() 
# Matrix b = new Matrix(10, 5)  // 10 rows, 5 columns
# b.input()
# Matrix c1 = a.add(b)
# Matrix c2 = a.subtract(b)
# Matrix c3 = a.transpose()
# a.print()