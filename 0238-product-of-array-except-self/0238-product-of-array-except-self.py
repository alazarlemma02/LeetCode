class Solution(object):
    def productExceptSelf(self, nums):
        pp = [1]
        sp = 1
        for num in range(1,len(nums)):
            pp.append(nums[num-1]*pp[-1])
        curr = len(nums) - 1
        while curr >= 0:
            pp[curr] *= sp
            sp *= nums[curr]
            curr -= 1
        return pp  
        