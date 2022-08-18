def dNums(A, B):

    n = len(A)
    freq = {}
    res = []

    for i in range(B):
        if A[i] in freq:
            freq[A[i]] += 1
        else:
            freq[A[i]] = 1
    res.append(len(freq))

    i = 1
    j = B

    while i <= n-B:

        freq[A[i - 1]] -= 1

        if freq[A[i - 1]] == 0:
            freq.pop(A[i-1])

        if A[j] in freq:
            freq[A[j]] += 1
        else:
            freq[A[j]] = 1

        res.append(len(freq))
        
        i += 1
        j += 1
    return res

A = [1, 2, 1, 3, 4, 3]
B = 3
print(dNums(A,B))
