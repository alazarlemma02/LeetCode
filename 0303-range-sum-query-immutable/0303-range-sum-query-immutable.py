class NumArray(object):

    def __init__(self, nums):
        self.p_nums = []
        first_elt = 0
        for num in nums:
            first_elt += num
            self.p_nums.append(first_elt)
        

    def sumRange(self, left, right):
        if left-1>=0:
            ls = self.p_nums[left-1]
        else:
            ls = 0
        return self.p_nums[right] - ls
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)