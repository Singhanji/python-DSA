# Function to take input from user
def inp(r, c):
    mat = [[int(input()) for x in range(c)] for y in range(r)]

    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = ' ')
        print()


"""
    r = int(input())
    c = int(input())

    mat=[]
    for i in range(r):
        a = []
        for j in range(c):
            a.append(int(input()))
        mat.append(a)

# Function to print the matrix

for i in range(r):
    for j in range(c):
        print(mat[i][j], end = ' ')
    print()

"""

r = int(input())
c = int(input())

inp(r, c)
