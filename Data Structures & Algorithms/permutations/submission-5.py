class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        seen = set()
        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return 
            for num in nums: 
                if not num in seen: 
                    path.append(num)
                    seen.add(num)
                    dfs(path)
                    path.pop()
                    seen.remove(num)
        dfs(path)
        return res