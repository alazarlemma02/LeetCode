class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        else:
            val = n
            while val % 3 == 0:
                val /= 3
            return True if val==1 else False
        