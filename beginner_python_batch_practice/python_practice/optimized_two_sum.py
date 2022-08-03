def twosum(nums,target):
    n = len(nums)
    a = nums[0]
    for i in range(n):
        if a + nums[i]== target:
            return i,a



#nums = [2,7,11,15]
nums = [2, 5, 5, 11]
target = 10
print(twosum(nums,target))
