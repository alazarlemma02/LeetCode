class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        counter = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                counter +=1
        return counter
        