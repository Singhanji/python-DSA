def SearchElement(A, B):
    found = 0
    n = len(A)
    for i in range(n):
        A[i] = int(A[i])
        if A[i] == B:
            found = 1
    print(found)

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    testCases = int(input())

    while testCases > 0:

        for _ in range(testCases):
            n = list(map(int, input().split()))

        k = int(input())

        SearchElement(n, k)
        testCases -= 1
    return 0


if __name__ == '__main__':
    main()