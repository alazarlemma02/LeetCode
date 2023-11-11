class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        result = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                result += 1
        return result
        