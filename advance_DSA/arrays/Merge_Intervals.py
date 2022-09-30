def insert(intervals, newInterval):
#    n = len(intervals)
    res = []
    t = []
    for i in intervals:
        print(f'i: {i}')
        A = range(i[0],i[1])
        print(A)
        if newInterval[0] in A or newInterval[1] in A:               
            t.append(min(i[0],newInterval[0]))
            t.append(max(i[1],newInterval[1]))
            res.append(t)
        else:
            res.append(i)
    return res

#A = [[1,3], [6,9]]
#B = [2,5]
A = [ (1, 2), (3, 6) ]
B = (10, 8)
print(insert(A,B))

