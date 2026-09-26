class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 1

        while i < len(prices):
            minCost = min(prices[0 : i])
            profit = prices[i] - minCost
            maxProfit = max(maxProfit, profit)
            i = i + 1
        return maxProfit