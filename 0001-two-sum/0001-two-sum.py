class Solution(object):
    def twoSum(self, nums, target):
        target_map = {}
        result = []
        for num in range(len(nums)):
            if target-nums[num] in target_map:
                result.append(nums.index(target-nums[num]))
                result.append(num)
                return result
            elif nums[num] not in target_map:
                target_map[nums[num]] = 1
            else:
                target_map[nums[num]] += 1
        