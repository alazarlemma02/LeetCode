class Solution(object):
    def isIsomorphic(self, s, t):
        d = {}
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if ch1 not in d:
                if ch2 in d.values(): return False
                d[ch1]=ch2
            elif d[ch1] != ch2: return False
        return True