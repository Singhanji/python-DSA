INT_MAX = (1<<31)-1

INT_MIN = -(1<<31)


    # @param A : integer

    # @param B : integer

    # @return an integer

def divide(A, B):

    n = A
    m = B
    sign = 1

    if (A < 0 and B > 0) or (A > 0 and B < 0):

        sign = -1
        n = abs(n)
        m = abs(m)
        q = 0
        t = 0

        for i in range(31, -1, -1):

            if t + (m << i) <= n:

                t += m << i

                q += 1 << i

        if sign < 0: 

            q = -q

        if q >= INT_MAX or q < INT_MIN:

            return INT_MAX

        return q

A = -2075698975
B = -1

print(divide(A,B))