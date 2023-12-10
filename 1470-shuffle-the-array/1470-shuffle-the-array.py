class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for num in range(n):
            result.append(nums[num])
            result.append(nums[num+n])
        return result
        

        