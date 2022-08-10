# Given N array elements, Check if they all are distinct or not
# TC: O(N)
# SC: O(N)

def dis(ar):

    n = len(ar)
    s = set()
    

    for i in range(n):
        s.add(ar[i])
    return s     
    

    if(dis(ar) == n):
        return True
    return False




# Driver code

ar = [1, 2, 3, 4]
print(dis(ar))

