class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        best_count = 0
        for i in nums:
            count = 1
            if not i-1 in seen:
                while i+1 in seen:
                    count+=1
                    i+=1
            best_count = max(count, best_count)
        return best_count
