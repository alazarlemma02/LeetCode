class Solution(object):
    def mySqrt(self, x):
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                result = mid
            else:
                high = mid - 1
        return result
        