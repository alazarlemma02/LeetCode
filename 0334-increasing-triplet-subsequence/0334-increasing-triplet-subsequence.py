class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 2: return False
        left_min = [nums[0]]
        right_max = [nums[-1]]
        
        for i in range(1,len(nums)):
            left_min.append(min(left_min[-1], nums[i]))
            
        for i in range(1,len(nums)):
            right_max.append(max(right_max[-1], nums[len(nums)-i-1]))
            
        right_max.reverse()
        for i in range(len(nums)):
            if left_min[i]<nums[i]<right_max[i]: return True
        return False
        