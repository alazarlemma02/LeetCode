class Solution(object):
    def searchInsert(self, nums, target):
        min , max = 0, len(nums)-1
        while min <= max:
            mid = (min+max)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                max = mid -1
            else:
                min = mid +1
        return min
            
        