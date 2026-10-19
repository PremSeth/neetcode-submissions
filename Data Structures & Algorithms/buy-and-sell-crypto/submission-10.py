class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profit = 0
        for i in prices: 
            profit = max(profit, i-cheapest)
            cheapest = min(i, cheapest)
        return profit
            
