class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        speed = (left + right) //2
        best = (0, math.inf)
        count = 0
        if len(piles) == h: 
            return max(piles)
        while left <= right: 
            time = 0
            for bans in piles: 
                time += math.ceil(bans/speed)
            if time <= h: 
                print(left, right, speed, time)
                right = speed-1
                if h-time <= h-best[0]:
                    best = (time, min(best[1], speed))
                print(best)
                speed = (left + right) //2
            else: 
                left = speed+1
                speed = (left + right) //2
        print(best)
        return best[1]
            


