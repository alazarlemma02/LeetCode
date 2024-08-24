class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 2: return False
        fs = float("inf")
        sc = float("inf")
        for i in range(len(nums)):
            if nums[i] <= fs: fs = nums[i]
            elif nums[i] <= sc: sc = nums[i]
            else: return True
        return False
        