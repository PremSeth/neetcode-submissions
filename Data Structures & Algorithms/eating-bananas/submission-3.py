class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)
        solutions = []
        while left <= right: 
            speed = (left+right)//2
            hours = 0
            for i in piles: 
                hours+=math.ceil(i/speed)
            if hours <= h: 
                solutions.append(speed)
                right = speed-1
            else: 
                left = speed + 1
            print(speed)
        return min(solutions)
        