class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        maxProfit = 0

        while i < len(prices):
           minCost = min(prices[0:i])
           profit = prices[i] - minCost
           maxProfit = max(profit, maxProfit)
           i = i + 1
        return maxProfit
           