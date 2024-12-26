class Solution(object):
    def findTheDifference(self, s, t):
        for i in range(len(t)):
            if s.count(t[i]) != t.count(t[i]):
                return t[i]
