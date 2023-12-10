class Solution(object):
    def smallestEvenMultiple(self, n):
        result, isTrue = 0, True
        while isTrue:
            result +=1
            if (n * result) % 2 == 0:
                isTrue = False
                result = n * result
        return result
                