# Given an array with N objects colored red, white, or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.
# Note: Using the library sort function is not allowed.

def sortColors(A):
    l = 0
    m = 0
    h = len(A) - 1

    while m <= h:
        print('m:', m)
        print('h:', h)
        if A[m] == 1:
            m += 1

        elif A[m] == 0:
            temp = A[m]
            A[m] = A[l]
            A[l] = temp
            m += 1
            l += 1
        elif A[m] == 2:
            temp1 = A[m]
            A[m] = A[h]
            A[h] = temp1
            h -= 1
    return A


A = [0, 1, 2, 0, 1, 2]
print(sortColors(A))
