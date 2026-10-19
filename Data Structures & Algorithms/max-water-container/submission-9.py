class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0
        while left < right: 
            hl = heights[left]
            hr = heights[right]
            min_h = min(hl, hr)
            water = min_h*(right-left)
            max_water = max(water, max_water)
            if hl < hr: 
                left +=1
            else: 
                right -=1
        return max_water