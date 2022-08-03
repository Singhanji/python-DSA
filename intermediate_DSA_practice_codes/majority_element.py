class Solution:

    # @param A : tuple of integers

    # @return an integer

    def repeatedNumber(A):

        n = len(A)
        if n == 1:
            return A[0]

        else:
            ele1=-1
            ele2=-1
            freq1, freq2 = 0, 0

            for i in range(n):
                if ele1 == A[i]:
                    freq1 += 1

                elif ele2 == A[i]:
                    freq2 += 1

                elif (freq1 == 0):
                    ele1 = A[i]
                    freq1+=1

                elif (freq2 == 0):
                    ele2 = A[i]
                    freq2+=1

                else:
                    freq1 -= 1
                    freq2 -= 1

            f1=0

            f2=0

            for i in A:

                if i==ele1:

                    f1+=1

                if i==ele2:

                    f2+=1

            if f1 > n//3:

                return ele1

            if f2 > n//3:

                return ele2

            return -1    

   # A = [1, 2, 3, 1, 1]
   # A =  [1000441, 1000441, 1000994]
    A = [1, 1, 1, 2, 3, 5, 7]
    print(repeatedNumber(A))

            