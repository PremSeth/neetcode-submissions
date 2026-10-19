class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def sub(start, path):
            if start > len(nums):
                return
            res.append(path.copy())
            for idx in range(start, len(nums)):
                path.append(nums[idx])
                sub(idx+1, path)
                path.pop()
            return
        sub(0, path)
        return res