class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i,j in enumerate(nums):
            if farthest < i:
                return False
            farthest = max(farthest, i+j)
        if farthest >= len(nums)-1:
            return True
        return False