class Solution(object):
    def majorityElement(self, nums):
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i]=1
            if len(nums) // 2 < counts[i]:
                return i
                
        