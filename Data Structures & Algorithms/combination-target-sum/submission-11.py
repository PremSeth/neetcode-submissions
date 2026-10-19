class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(start, path):
            if sum(path) == target: 
                res.append(path.copy())
                return 
            if sum(path) > target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, path)
                path.pop()
        dfs(0, path)
        return res