class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        left, right = 0, len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left +=1
                right +=1
        return -1
        