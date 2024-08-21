class Solution(object):
    def findShortestSubArray(self, nums):
        map = {}
        max_deg = 0
        min_len = len(nums)
        for num in range(len(nums)):
            if nums[num] in map:
                map[nums[num]][0] += 1
                map[nums[num]][2] = num
            else:
                map[nums[num]] = [1,num, num]

            if map[nums[num]][0] > max_deg:
                max_deg = map[nums[num]][0]
                min_len = map[nums[num]][2]-map[nums[num]][1] + 1
            elif map[nums[num]][0] == max_deg:
                length = map[nums[num]][2]-map[nums[num]][1] + 1
                min_len = min(length, min_len)
        return min_len
        