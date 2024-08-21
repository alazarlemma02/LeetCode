class Solution(object):
    def findShortestSubArray(self, nums):
        map = {}
        max_deg = 1
        min_len = len(nums)
        for num in range(len(nums)):
            if nums[num] in map:
                map[nums[num]][0] += 1
                map[nums[num]][2] = num
            else:
                map[nums[num]] = [1,num, num]

            max_deg = max(map[nums[num]][0], max_deg)

        for num in map:
            if map[num][0] == max_deg:
                dis = map[num][2] - map[num][1] + 1
                min_len = min(dis, min_len)

        return min_len
        