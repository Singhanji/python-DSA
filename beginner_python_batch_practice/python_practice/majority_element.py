#  Majority Element: Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times.
# Arrays & Maths

def MajorityElement(A):
    element = A[0]
    frequency = 1
    n = len(A)

    for i in range(1,n):
        if frequency == 0:
            element = A[i]
            frequency = 1

        elif element == A[i]:
            frequency += 1
        else:
            frequency -= 1

    return element



A = [3, 4, 4, 8, 4, 9, 4, 3, 4]
print(MajorityElement(A))

