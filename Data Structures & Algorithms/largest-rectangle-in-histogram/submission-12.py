class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        max_area = -1*math.inf
        for i in range(len(heights)): 
            print(area)
            area = heights[i]
            for j in range(i-1, -1, -1): 
                if heights[j] >= heights[i]:
                    area += heights[i]
                    print(area)
                else: 
                    break
            for j in range(i+1, len(heights)):
                if heights[j] >= heights[i]:
                    area += heights[i]
                    print(area)
                else: 
                    break
            max_area = max(max_area, area)
        return max_area
