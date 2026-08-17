class Solution:
    def maxProfit(self, prices):
        low = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(profit, prices[i] - low)

        return profit