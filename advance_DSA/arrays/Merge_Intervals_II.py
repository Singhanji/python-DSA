# 2nd Approach
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


    def insert(self, intervals, newInterval):
        n = len(intervals)
        res = []
        for i in range(n):
       
            if newInterval.start > intervals[i].end:
                res.append(intervals[i])
            elif intervals[i].start > newInterval.end:
                res.append(newInterval)

                k = i
                while k < n:
                    res.append(intervals[k])
                    k += 1
                return res
            else:
                newInterval.start = min(newInterval.start,intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)

        res.append(newInterval)
        return res

A = [[1,3], [6,9]]
B = [2,5]
c = Interval(A,B)
print(c.insert(A, B))


