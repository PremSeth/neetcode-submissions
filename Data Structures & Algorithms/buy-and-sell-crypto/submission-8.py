class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = math.inf
        profit = 0
        for i in prices: 
            profit = max(profit, i-cheapest)
            cheapest = min(i, cheapest)
        return profit
            
