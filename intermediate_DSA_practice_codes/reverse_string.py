# You are given a string A of size N.

# Return the string A after reversing the string word by word.

# NOTE:

# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.

def rev_string(A):
    n = len(A)
    print('n:', n)
    ans = ''
    cur = ''
    rev = ''
    for i in range(n-1,-1,-1):
        if (A[i] != ' '):
            cur += A[i]
            print('cur', cur)
            cur[::-1]
                    
            
        if not ans == '':
            ans += ' '
        ans += cur
        print('ans: ', ans)

    return ans


A = "sky is blue  "
print(rev_string(A))

