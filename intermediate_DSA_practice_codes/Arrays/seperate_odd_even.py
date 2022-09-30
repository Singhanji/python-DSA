def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    testCases = int(input())
    while(testCases > 0):
    
        for _ in range(testCases):
            n = int(input())
            A = list(map(int, input(). split()))
            even = []
            odd = []
    
            for i in A:
                if i & 1 != 1:
                    even.append(i)
                elif i & 1 == 1:
                    odd.append(i)
            for i in odd:
                print(i, end = ' ')
            print()
            for i in even:
                print(i, end = ' ')

            print()
            testCases -= 1
        
if __name__ == '__main__':
    main()