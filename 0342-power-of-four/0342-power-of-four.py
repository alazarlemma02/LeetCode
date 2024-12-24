class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        else:
            val = n
            while val % 4 == 0:
                val /= 4
            return True if val==1 else False
        