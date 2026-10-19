class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []
        def dfs(start, path):
            if start > len(nums):
                return
            res.add(tuple(sorted(path)))
            for idx in range(start, len(nums)):
                path.append(nums[idx])
                dfs(idx+1, path)
                path.pop()
        dfs(0, path)
        return list(res)