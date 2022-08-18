def solve(A,B):

    hm = {}
    n = len(A)
    m = len(B)

    for i in range(n):
        hm[A[i]] = i
    print(hm)

    for i in range(1,m-1):

        if B[i] == A[i]:
            print(hm[A[i]])
            return True
        else:
            return False



A = "adhbcfegskjlponmirqtxwuvzy"
B = ["hello", "scaler", "interviewbit"]
print(solve(A, B))