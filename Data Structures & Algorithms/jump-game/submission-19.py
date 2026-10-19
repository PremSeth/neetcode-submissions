class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = set()
        def dfs(idx):
            seen.add(idx)
            if idx >= len(nums)-1: 
                return True
            for i in range(1, nums[idx]+1):
                if not idx+i in seen and dfs(idx+i):
                    return True
            return False
        return dfs(0)
