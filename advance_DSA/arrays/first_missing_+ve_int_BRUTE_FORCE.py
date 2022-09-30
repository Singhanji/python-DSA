def solve(A):
    arr = sorted(A)
    print(arr)    
    n = len(A)
    print(n)
    for i in range(1, n):
        if arr[i] < 0:
            i += 1
        return 1

    for i in range(1,n+1):
        print(f'i: {i} arr[i-1]: {arr[i-1]}')
        if arr[i] < 0:
            print(f'arr[i] : {arr[i]}')
            print('here')
            i += 1
        if i != arr[i]:
            return i   
        
    return i+1
        

#A = [1, 2, 0]
#A = [-1, 1, 3, 4]
A = [3, 4, -1, 1]
#A = [-8, -7, -6]
print(solve(A))
