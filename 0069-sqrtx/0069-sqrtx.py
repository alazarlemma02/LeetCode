class Solution(object):
    def mySqrt(self, x):
        if x==0 or x==1:
            return x
        left, right, result = 0, x-1, x
        while left <= right:
            mid = (left + right)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid -1
            else:
                left = mid + 1
                result = mid
        return result
        
        