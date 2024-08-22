class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        s_prod = p_prod = 1
        for num in range(len(nums)):
            if p_prod == 0:
                p_prod = 1
            if s_prod == 0:
                s_prod = 1
            p_prod *= nums[num]
            s_prod *= nums[len(nums)-num-1]
            max_prod = max(max_prod, max(p_prod, s_prod))
        return max_prod
        