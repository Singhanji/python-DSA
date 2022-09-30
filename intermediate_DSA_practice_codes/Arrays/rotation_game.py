def swap(arr, s, e):
    while(s<e):
        arr[s],arr[e] = arr[e],arr[s]
        s += 1
        e -= 1

def rotate_by_k_times(arr, k):
    n = len(arr)

    swap(arr, 0, n-1)
    swap(arr, 0, k-1)
    swap(arr, k, n-1)

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    temp = input().split()

    N = int(temp[0])

    A = [0] * N

    for i in range(1, N + 1):

        A[i - 1] = int(temp[i])

    B = int(input())
    B = B % N
    
    rotate_by_k_times(A, B)
    for i in A:
        print(i, end=' ')

if __name__ == '__main__':
    main()