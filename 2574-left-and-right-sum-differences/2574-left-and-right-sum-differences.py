class Solution(object):
    def leftRightDifference(self, nums):
        answer = []
        for num in range(len(nums)):
            ls = 0
            rs = 0
            i = num - 1
            j = num + 1
            while i >= 0:
                ls += nums[i]
                i -= 1
            while j < len(nums):
                rs += nums[j]
                j += 1
            answer.append(abs(ls-rs))
        return answer
        