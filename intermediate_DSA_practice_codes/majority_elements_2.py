# Program to find two Majority elements, that appears more than floor(n/3) times.

def MajorityElements2(A):
    ele1, ele2 = A[0], A[1]
    freq1, freq2 = 1, 1
    n = len(A)

    for i in range(n):
        if (freq1 == 0):
            ele1 = A[i]
            freq1 = 1
        
        elif (freq2 == 0):
            ele2 = A[i]
            freq = 1

        elif ele1 == A[i]:
            freq1 += 1

        elif ele2 == A[i]:
            freq2 += 1

        else:
            freq1 -= 1
            freq2 -= 1

    return ele1, ele2


A = [5, 6, 5, 5, 6, 3, 6]
print(MajorityElements2(A))

