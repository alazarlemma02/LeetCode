class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        p_prod = nums[0]
        for num in range(1, len(nums)):
            if p_prod == 0:
                p_prod = 1
            p_prod *= nums[num]
            if p_prod > max_prod:
                max_prod = p_prod

        s_prod = nums[-1]
        for num in range(1, len(nums)):
            if s_prod > max_prod:
                max_prod = s_prod
            if s_prod == 0:
                s_prod = 1
            s_prod *= nums[len(nums)-num-1]


        return max_prod
        