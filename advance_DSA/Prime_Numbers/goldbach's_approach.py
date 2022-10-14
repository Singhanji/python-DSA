
def primesum(A):
    if A == 4: return [2,2]

    # Creating Prime Bool Seive    
    def creatseive(n):
        pf = [True] * (n)
        pf[0] , pf[1] = False , False
        i = 2
        while i * i  < n:
            if pf[i] == True:
                j = i * i
                while j < n:
                    pf[j] = False
                    j +=i
            i +=1
               
        return pf
           
    spf = creatseive(A+1)

    # Using Two Pointer x Goldbach's conjecture Approach 
    i = 2
    j = A - 2

    while i < j:
        if spf[i] and spf[j]:
            cur_sum = i + j
            if cur_sum == A:
                arr = [i,j]
                return arr
        i += 1
        j -= 1

A = 14
print(primesum(A))