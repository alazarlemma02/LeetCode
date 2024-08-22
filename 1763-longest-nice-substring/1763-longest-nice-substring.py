class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""
        s_set = set(s)
        for i in range(len(s)):
            if s[i].lower() not in s_set or s[i].upper() not in s_set:
                ns_p = self.longestNiceSubstring(s[:i])
                ns_s = self.longestNiceSubstring(s[i+1:])
                return ns_s if len(ns_p) < len(ns_s) else ns_p
        return s
        