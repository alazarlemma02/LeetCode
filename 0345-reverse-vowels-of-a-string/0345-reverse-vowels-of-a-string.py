class Solution(object):
    def reverseVowels(self, s):
        r_s = ""
        s_s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for v in s:
            if v in vowels:
                r_s += v
        n = -1
        for i in range(len(s_s)):
            if s_s[i].lower() in vowels:
                s_s[i]=r_s[n]
                n -= 1
        return "".join(s_s)