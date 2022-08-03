# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return i,j


nums = [2,5,5,11]
target = 10
print(twoSum(nums,target))
