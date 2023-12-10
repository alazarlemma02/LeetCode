class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []
        while left <= right:
            status = 0
            for i in str(left):
                if int(i)!=0 and left % int(i) ==0:
                    status +=1
            if status == len(str(left)):
                result.append(left)
            left += 1
        return result

            