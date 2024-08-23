class Solution(object):
    def reverseVowels(self, s):
        s_s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(s_s)-1
        while start < end:
            if s_s[start] in vowels and s_s[end] in vowels:
                temp=s_s[end]
                s_s[end]=s_s[start]
                s_s[start]=temp
                start +=1
                end -=1
            elif s_s[start] not in vowels: 
                start+=1
            else: 
                end-=1

        return "".join(s_s)