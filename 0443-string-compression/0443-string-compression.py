class Solution(object):
    def compress(self, chars):
        left = right = 0
        while right < len(chars):
            curr = chars[right]
            count = 1
            while right < len(chars)-1 and chars[right+1]==curr:
                right +=1
                count +=1
            chars[left] = curr
            left +=1
            if count > 1:
                for c in str(count):
                    chars[left] = c
                    left +=1
            right +=1
        return left
        