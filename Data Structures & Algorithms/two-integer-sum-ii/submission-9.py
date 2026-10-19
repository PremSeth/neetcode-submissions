class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)): 
            if numbers[i] in seen: 
                return [seen[numbers[i]]+1, i+1]
            seen[target-numbers[i]] = i
