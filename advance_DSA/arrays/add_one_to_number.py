# Add one to number  [1, 2, 3] + 1 = [1, 2, 4]
# [9, 9, 9] + 1 = [1, 0, 0, 0]


def plusOne(nums):
   i = len(nums) - 1
   while i >= 0:
      if nums[i] + 1 <= 9:
         nums[i] = nums[i] + 1
         break
      else:
         nums[i] = 0
      i -= 1
   if i < 0:
      nums.insert(0, 1)
   count = 0
   if len(A) > 1: 
      for k,v in enumerate(A):
         if v == 0:
            count = k
         else:
            break
      return A[count+1::]
   
   return A
#A = [1, 2, 3]
#A = [9, 9, 9]
#A = [0, 3, 7, 6, 4, 0, 5, 5, 5]
#A = [0]
#A = [1, 2, 4]
#A = [0, 0, 4, 4, 6, 0, 9, 6, 5, 1]
A = [2, 5, 6, 8, 6, 1, 2, 4, 5]
print(plusOne(A))