class Solution(object):
    def twoSum(self, nums, target):
        target_map = {}
        result = []
        for num in range(len(nums)):
            if target-nums[num] in target_map:
                result.append(target_map[target-nums[num]])
                result.append(num)
                return result
            if nums[num] not in target_map:
                target_map[nums[num]] = num

        