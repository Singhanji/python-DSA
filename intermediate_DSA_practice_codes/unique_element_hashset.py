# Find number of distinct elements
# TC: O(N)
# SC: O(N)

def countofuniqset(ar):
    n = len(ar)
    uniq = set()  # creating an empty set

    for i in range(n):
        uniq.add(ar[i])
    return len(uniq)


def countofUniqueShort(ar):
    uniq = set(ar)
    return len(uniq)


ar = [6, 2, 4, 7, 4, 4, 2, 6, 1]
print(countofuniqset(ar))
print(countofUniqueShort(ar))
