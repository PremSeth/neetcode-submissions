class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def csum(start, combo):
            if sum(combo) == target: 
                result.append(combo.copy())
                return
            if sum(combo) > target: 
                return

            for idx in range(start, len(nums)): 
                combo.append(nums[idx])
                csum(idx, combo)
                combo.pop()
        csum(0, path)
        return result