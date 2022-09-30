def k_symbol(row, col):
    
    for i in range(1,row):
        print(i)
        if i == 1:
            row[i] = 0
        if row[i-1] == 0:
            row[i] = '01'
        else:
            row[i] = '10'

row = 2
col = 1
print(k_symbol(row,col))
