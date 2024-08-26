class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)==0:
            return True
        left = right = 0
        while left < len(s) and right < len(t):
            if s[left]==t[right]:
                left +=1
                right +=1
            else:
                right +=1
            if left == len(s):
                return True
        return False
        