class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        hl = 0
        hr = 0
        while left < right:
            hl = max(hl, height[left])
            hr = max(hr, height[right])
            print(hl, hr, water)
            if hl < hr: 
                water+=max(hl-height[left], 0)
                left+=1
            else: 
                water+=max(hr-height[right], 0)
                right-=1
        return water
        
            