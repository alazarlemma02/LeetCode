class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        i = 0
        largest = len(word1) if len(word1) > len(word2) else len(word2)
        while i < largest:
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
            i+=1
        return result
        