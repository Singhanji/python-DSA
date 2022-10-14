# Sorting: Arranging data in increase/decrease order based on parameter.
- 1 2 3 4 5 7 : increasing order; parameter = value
- 9 8 6 5 4 3 : decreasing order; parameter = value
- 1 7 2 9 24  : increasing order; parameter = no. of factors

# Why Sorting?
- Searching becomes easier

# What is Stable/Unstable Sorting?
- When 2 data points have same parameter value and their relative order is same after sorting also are called Stable Sorting, else Unstable Sorting.    
- Eg:  NAME     MARKS
       Mohit      0
       Aman      100
       Shrest    45 
       Kajal     32 
       Ayush     45
       Aditya    92
    In the above example, Shrest and Ayush have same marks so after sorting, Shrest will come first and then Ayush, such that there relative order is same before and after sorting this type of sorting is called stable sorting.

# Inplace Sorting?
- If sorting algo takes O(1) space in that case it is considered as Inplace Sorting.

# Selection Sort: 
- The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from the unsorted part and putting it at the beginning. 

    The algorithm maintains two subarrays in a given array.

    - The subarray which already sorted. 
    - The remaining subarray was unsorted.
    - In every iteration of the selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

- It is an Inplace Sorting Algorithm. So it takes O(1) SC.
- It is not stable Algorithm.
- TC: O(N*N)

# Eg: 	def kthsmallest(A, B):
        A = list(A)
        n = len(A)
        for i in range(B):  
            min_v = A[i]
            idx = i
            for j in range(i, n):
                if A[j] < min_v:
                    min_v = A[j]
                    idx = j
            A[idx],A[i] = A[i],A[idx]
        
        return A[B-1]


# Bubble Sort:
- Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
