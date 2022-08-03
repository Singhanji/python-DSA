def numSetBits(A):
        c = 0
        while(A != 0):
            rem = A % 2
            print("rem:", rem)
            if rem == 1:
                c += 1
                print("Value of count", c)
            A = A // 2
            print("Val of A:", A)
            print("-------------------")
        print(c)
        

A = 11
print(numSetBits(A))
