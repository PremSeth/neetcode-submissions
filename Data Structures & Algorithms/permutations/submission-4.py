class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for num in nums: 
                if not num in path: 
                    path.append(num)
                    dfs(path)
                    path.pop()
        dfs(path)
        return res