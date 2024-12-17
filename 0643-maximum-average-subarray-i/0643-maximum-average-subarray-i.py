class Solution(object):
    def findMaxAverage(self, nums, k):
        n, m = 0, k
        curr_sum = sum(nums[n:m])
        max_sum = curr_sum
        while m < len(nums):
            curr_sum -= nums[n]
            n += 1
            
            curr_sum += nums[m]
            m += 1
            
            max_sum = max(curr_sum, max_sum)
        return max_sum / float(k)