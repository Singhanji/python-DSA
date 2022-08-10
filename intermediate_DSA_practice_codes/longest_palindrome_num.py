# Given a string A of size N, find and return the longest palindromic substring in A. Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string: A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A. Incase of conflict, return the substring which occurs first ( with the least starting index).


def LongestString(s,p1,p2):

    n = len(s)
    A = ''
    while(p1 >= 0 and p2 < n and s[p1] == s[p2]):
        p1 -= 1
        p2 += 1
        
#        if p1 > 1:
#            print(f'{p1}: {p2}, {s[p1]}: {s[p2]}')
        r = p2 - p1 - 1
        print(r)
    A = s[p1+1:p2]
    print(A)
    return A

   


def lps(s):

    n = len(s)
    ans = s[0]
    
    if n & 1 == 1:
        for i in range(n):

            p1 = i
            p2 = i
            r = LongestString(s, p1, p2)
            if len(r) > len(ans):
                o = r
            else:
                o = ans
    else:
        for i in range(n):
            p1 = i
            p2 = i + 1
            r = LongestString(s, p1, p2)
            if len(r) > len(ans):
                o = r
            else:
                o = ans

    return o


# Driver Code

#s = "aaaabaaa"
s = "aaabaaa"
#s = 'caba'
print(lps(s))




