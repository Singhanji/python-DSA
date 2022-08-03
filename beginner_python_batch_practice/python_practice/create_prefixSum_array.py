# Create prefix sum array

def prefix_Sum_Array(A,n,PfSum):
    PfSum[0] = A[0]

    for i in range(1,n):
        PfSum[i] = PfSum[i-1] + A[i]
#        print(PfSum[i], end=" ")

# Driver Code
A = [10, 20, 30, 40]
n = len(A)
