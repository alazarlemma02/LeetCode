class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        if len(candies)<2:
            return [True]
        max_val = candies[0]
        for can in candies:
            if can > max_val:
                max_val = can
        for can in range(len(candies)):
            if candies[can] + extraCandies >= max_val:
                candies[can] = True
            else:
                candies[can] = False
        return candies
            
        