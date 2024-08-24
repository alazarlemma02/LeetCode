class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        return " ".join(reversed(s))
        