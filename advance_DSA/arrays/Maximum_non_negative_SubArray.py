def maxSet(A):
    
    max_Sum = -1
    cur_Sum = 0
    n = len(A)
    s = 0
    start = 0
    end = -1 

    for i in range(n):
        if (A[i] < 0):
            s = i + 1
            cur_Sum = 0
        else:
            cur_Sum += A[i]
        if cur_Sum > max_Sum:
            if cur_Sum == max_Sum:
                if(i-s+1)<start+end+1:
                    continue
            max_Sum = cur_Sum
            start = s
            end = i
        if end == -1:
            return []
        
    return A[start:end+1]

#A = [1, 2, 5, -7, 2, 3]
#A = [10, -1, 2, 3, -4, 100]
A = [0, 0, -1, 0]
print(maxSet(A))