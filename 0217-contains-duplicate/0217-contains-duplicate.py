class Solution(object):
    def containsDuplicate(self, nums):
        map = {}
        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1
        return False
            
        