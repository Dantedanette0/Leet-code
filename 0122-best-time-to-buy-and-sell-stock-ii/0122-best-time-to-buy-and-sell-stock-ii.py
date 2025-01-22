class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                profits.append(prices[i] - prices[i-1])
        return sum(profits)
