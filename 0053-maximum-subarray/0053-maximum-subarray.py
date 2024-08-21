class Solution(object):
    def maxSubArray(self, nums):
        maximum = nums[0]
        sum = 0
        for i in nums:
            sum += i
            if sum > maximum:
                maximum = sum
            if sum < 0:
                sum = 0            
        return maximum
        