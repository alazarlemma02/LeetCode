class Solution(object):
    def firstUniqChar(self, s):
        MAP = {}
        for i in range(len(s)):
            if s[i] in MAP:
                MAP[s[i]][0] +=1
            else:
                MAP[s[i]] = [1, i]
                
        ans = len(s)
        current = MAP[s[0]][1]
        for val in MAP:
            if MAP[val][0] == 1:
                ans = min(ans, MAP[val][1])
        return ans if ans != len(s) else -1
                

        
        
        