'''class Solution:
    def maxProfit(self, prices):
        low = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                profit = max(profit, prices[i] - low)

        return profit'''
#kadane algorithm
class Solution:
    def maxProfit(self, prices):
        current = 0
        maximum = 0

        for i in range(1, len(prices)):
            current += prices[i] - prices[i - 1]

            if current < 0:
                current = 0

            maximum = max(maximum, current)

        return maximum