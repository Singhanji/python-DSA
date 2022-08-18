def colorful(A):
    A = str(A)      # convert given integer into String
    n = len(A)      # len of String
    hs = set()       # consider an hashset
    for i in range(n):   # traverse in String
        prod = 1           # consider product initially=1
        for j in range(i, n):    # nested loop in range i to len of String
            prod = prod * int(A[j])    # calculate product of each elem
            if(prod in hs):          # check product in hashset
                return 0        # if prod available return 0
            else:                 # if prod not available then add in hashset
                hs.add(prod)
        return 1     # return 1 if prod isnt available in hashset
    
A = 23
print(colorful(A))