class Solution(object):
    def repeatedCharacter(self, s):
        output = ""
        for i in s:
            if i in output:
                return i
            else:
                output+=i
        