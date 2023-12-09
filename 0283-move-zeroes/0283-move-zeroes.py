class Solution(object):
    def moveZeroes(self, nums):
        previous_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
               temp = nums[previous_index]
               nums[previous_index] = nums[i]
               nums[i] = temp
               previous_index+=1
               