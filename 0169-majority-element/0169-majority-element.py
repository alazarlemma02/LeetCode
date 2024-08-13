class Solution(object):
    def majorityElement(self, nums):
        count = len(nums) / 2
        ex = []
        for i in nums:
            if i not in ex:
                if nums.count(i) > count:
                    return i
            ex.append(i)
                
        