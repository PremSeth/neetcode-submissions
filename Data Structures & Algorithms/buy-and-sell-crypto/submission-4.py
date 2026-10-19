class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = math.inf
        best = 0
        for i in prices: 
            best = max(best, i-small)
            if i < small: 
                small = i
        return best