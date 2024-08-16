class Solution(object):
    def runningSum(self, nums):
        result = []
        result.append(nums[0])
        for i in range(1,len(nums)):
            k = nums[i] + result[-1]
            result.append(k)
        return result
            
            
        