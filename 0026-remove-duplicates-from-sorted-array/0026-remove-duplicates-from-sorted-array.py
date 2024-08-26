class Solution(object):
    def removeDuplicates(self, nums):
        left = right = 0
        while right < len(nums):
            curr = nums[right]
            while right < len(nums)-1 and nums[right+1]==curr:
                right +=1
            nums[left] = curr
            left +=1
            right +=1 
        return left
        
        