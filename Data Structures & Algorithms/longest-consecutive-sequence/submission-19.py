class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_length = 0
        current_length = 0
        for i in range(len(nums)): 
            curr = nums[i]
            current_length = 1
            if curr -1 not in seen: 
                while curr +1 in seen: 
                    curr +=1
                    current_length +=1
            max_length = max(max_length, current_length)
            current_length = 1
        return max_length
                
                    

