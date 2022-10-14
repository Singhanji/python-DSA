# What is Recursion?
- Function calling itself
- Solving a problem using Sub problem

# Three Steps to solve Recursion problems
- Make an Assumption: Decide what your function does and trust that it will do it.
- Main Logic: Solve the big problem using Sub problem
- Base condition: when your recursion should stops

# Sum of First Naturat Numbers?
- Sum(N) = 1+2+3+4+5....+(N-2)+(N-1)..+N
- Sum of all no. from 1 to N-1 = 1+2+3+4+5....+(N-2)+(N-1)
- Sum(N) = Sum(N-1) + N

# EXAMPLE 1: Pseudo code for "Sum of First Naturat Numbers"
Using above approach to solve this problem, step by step.

1. Assumption: Sum(N), this function will give us the sum of all natural numbers from 1 to N.
2. Main Logic: Sum(N) = Sum(N-1) + N
3. Base condition: if N == 1: return 1

    Sum(int N) {

        // Base condition
        if N == 1:
            return 1

        // Main Logic
        return Sum(N-1) + N
    }
# EXAMPLE 2: Factorial of N
N! = N * (N-1) * (N-2)...1
fact(N) = 1 * 2 * 3 * 4 * 5......... * (N-1) * N

1. Assumption: fact(N) gives me the factorial of N
2. Main Logic: fact(N-1) * N
3. Base condition: if N <= 1: return 1

        fact(int N){

            // Base condition
            if N == 0:
                return 1

            // Main Logic
            return fact(N-1) * N
        }

Note:
- N == 1, we did not pick this as base condition because it is already handled in main cond. 
    
    if N == 1
    1! = fact(N-1) * 1
    1! = fact(0) * 1
    1! = 1*1 = 1
But, for N == 0, main cond will get fails.
    if N == 0:
    0! = fact(0 -1) * 1
    0! = fact(-1) * 1    #this cond. will be fail so we will handle it in base condition. It will break apart

- fact(0) = 1 
Why? Reason is here: https://www.youtube.com/watch?v=X32dce7_D48

# EXAMPLE 2: Fibonacci Series: Given N compute Nth Fibonacci numbers
- FS = Given 'Fibonacci series', and its index N
- A series where the next term is nothing but Sum of previous 2 numbers.
N : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
FS: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...


# What to do?
- Return fibonacci of N, if N == 7: return 21

1. Assumption: fib(N) gives me the Nth fibonacci number
2. Main Logic: fib(N-1) + fib(N-2)
3. Base condition: if N == 0 or N == 1: return 1

    fib(int N) {

        // Base condition
        if N == 0 or N == 1:
            return 1
        
        // Main Logic
        return fib(N-1) + fib(N-2)
    }




    




