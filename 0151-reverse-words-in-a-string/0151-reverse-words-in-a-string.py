class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        res = ""
        words = []
        for word in s:
            if word !="":
                words.append(word)
        i = 0
        while i < len(words):
            res+=words[i]
            if i != len(words)-1:
                res+=" "
            i += 1
        return res
        