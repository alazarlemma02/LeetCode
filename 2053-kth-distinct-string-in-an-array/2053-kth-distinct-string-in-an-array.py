class Solution(object):
    def kthDistinct(self, arr, k):
        np = []
        for i in arr:
            if arr.count(i) == 1:
                np.append(i)
        if len(np)<k:
            return ""
        return np[k-1]
               