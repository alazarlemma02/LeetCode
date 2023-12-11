class Solution(object):
    def smallestEqual(self, nums):
        smallestIdx = -1
        for i in range(len(nums)):
            result = i%10
            if result == nums[i]:
                smallestIdx = i
                break
        return smallestIdx
        