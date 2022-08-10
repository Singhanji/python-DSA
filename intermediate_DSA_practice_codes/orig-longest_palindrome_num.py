# Given a string A of size N, find and return the longest palindromic substring in A. Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string: A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A. Incase of conflict, return the substring which occurs first ( with the least starting index).


def LongestString(s,p1,p2):

    n = len(s)
    A = ''
    while(p1 >= 0 and p2 < n and s[p1] == s[p2]):
        p1 -= 1
        p2 += 1
        
        if p1 > 1:
            print(f'{p1}: {p2}, {s[p1]}: {s[p2]}')
        r = p2 - p1 - 1
        l = s[p1] != s[p2]
        i = p1
        j = p2

    return s[i+1:j]

   


def lps(s):

    n = len(s)
    ans = s[0]

    for i in range(n):
        p1 = i
        p2 = i
        ans = max(ans, LongestString(s,p1,p2))
        
        p1 = i
        p2 = i + 1
        ans = max(ans, LongestString(s,p1,p2))

    return ans


# Driver Code

#s = "aaaabaaa"
#s = "aaabaaa"
s = 'caba'
print(lps(s))




