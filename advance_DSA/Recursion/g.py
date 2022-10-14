# Working perfectly - Gray code


def grayCode(A):
    def code(A):
        if A == 1:
            return [0, 1]  
        value = code(A-1)
        ans = value.copy()
        for i in range(len(value)-1, -1, -1):
            ans.append((1<<(A-1)) + value[i])
        return ans

           
    return code(A)


A = 2
print(grayCode(A))
