class Solution(object):
    def isValid(self, s):
        stack = []
        closingValues = [')' , ']', '}']
        openingValues = ['(', '[', '{']
        result = True
        for i in range(len(s)):
            if s[i] in openingValues:
                stack.append(s[i])
            elif s[i] in closingValues:
                if len(stack) == 0:
                    result =  False
                elif stack[-1] == openingValues[closingValues.index(s[i])]:
                    stack.pop()
                else:
                    result = False
        if len(stack) != 0:
            return False
        else:
            return result
        