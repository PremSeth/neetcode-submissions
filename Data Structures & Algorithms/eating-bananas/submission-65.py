class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        if h == len(piles):
            return max(piles)
        slowest = math.inf
        while left <= right: 
            mid = (left+right)//2
            time = 0
            for i in piles: 
                time += math.ceil(i/mid)
            if time <= h: 
                slowest = min(slowest, mid)
                right = mid - 1
            else: 
                left = mid + 1
        return slowest