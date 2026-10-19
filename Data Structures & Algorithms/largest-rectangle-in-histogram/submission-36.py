class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        idx = 0
        for index, height in enumerate(heights): 
            idx = index
            while stack and stack[-1][1] > height: 
                idx, h = stack.pop()
                largest = max(largest, h*(index-idx))
            stack.append((idx, height))
        while stack: 
            idx, h = stack.pop()
            largest = max(largest, h*(len(heights)-idx))
        return largest