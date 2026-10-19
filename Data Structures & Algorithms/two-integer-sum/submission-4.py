class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i,j in enumerate(nums): 
            if j in differences: 
                return [differences[j], i]
            differences[target-j] = i
