class Solution(object):
    def findTheDifference(self, s, t):
        # MAP = {}
        for i in range(len(t)):
            if s.count(t[i]) != t.count(t[i]):
                return t[i]
        #         MAP[t[i]] = [s.count(t[i]), t.count(t[i])]
        # for val in MAP:
        #     if MAP[val][0] != MAP[val][1]:
        #         return val
