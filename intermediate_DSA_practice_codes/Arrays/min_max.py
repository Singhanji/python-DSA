def min_max(A):
    n = len(A)
    min_v = float('inf')
    max_v = -float('inf')
    for i in range(1,n):
        if min_v > A[i]:
            min_v = A[i]
        elif max_v < A[i]:
            max_v = A[i]
    print(min_v, max_v, sep = ' ')



def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(map(int, input().split()))
    min_max(A)

if __name__ == '__main__':
    main()