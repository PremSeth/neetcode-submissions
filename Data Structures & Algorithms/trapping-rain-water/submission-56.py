class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)
        mL = 0
        mR = 0
        for i in range(len(height)):
            max_left[i] = mL
            mL = max(mL, height[i])
        for i in reversed(range(len(height))): 
            max_right[i] = mR
            mR = max(mR, height[i])
        total_water = 0
        for i in range(len(height)): 
            total_water += max(min(max_left[i], max_right[i])-height[i], 0)
        return total_water