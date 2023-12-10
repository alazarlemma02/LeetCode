class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        len1 = len(word1)
        len2 = len(word2)
        length = len1 + len2
        for i in range(length):
            if len1 > 0:
                result += word1[-1 * len1]
                len1-=1
            if len2 > 0:
                result += word2[-1 * len2]
                len2 -=1
        return result
        
        
        
        