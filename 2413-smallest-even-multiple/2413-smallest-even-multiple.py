class Solution(object):
    def smallestEvenMultiple(self, n):
        result = 0
        isTrue =  True
        multiplier = 1
        while isTrue:
            for i in range(1, n+1):   
                if 2 * i == n * multiplier:
                    result = n * multiplier
                    isTrue = False
            multiplier += 1
        return result
        