class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        buy_price = prices[0]
        for i in prices:
            if i < buy_price:
                buy_price = i
            else:
                profit = max(profit, i - buy_price)
        return profit
        