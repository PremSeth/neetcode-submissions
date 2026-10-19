class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0
        best = 0
        for i in seen: 
            if i-1 not in seen: 
                while i in seen: 
                    count +=1
                    i+=1
                best = max(count, best)
                count = 0
        return best