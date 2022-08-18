# Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at those indices in the array are equal.
# Shaggy wants you to find a special pair such that the distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1.

# TC: O(N)
# SC: O(N)

def solve(A):

    idx = {}
    n = len(A)

    for i in A:
        print(i)
        idx[i] = -1
        print(idx)

    res = 10^9
    for i in range(n):
        if idx[A[i]] != -1:
            res = min(res, i - idx[A[i]])
            print('res ', res)
            print(res)
        idx[A[i]] = i

  #  if res == 10^9:
  #      return -1
    return res


# Driver Code
A = [7, 1, 3, 4, 1, 7]
print(solve(A))
