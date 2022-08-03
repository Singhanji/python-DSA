def first_occurance(s,n):

    for char in s:
        if chr(n) == char:
            i = s.index(char)
            return i
    else:
        return -1

s = input()
n = int(input())
print(first_occurance(s,n))


