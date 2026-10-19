class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_count = 0
        for i in nums: 
            if i-1 not in seen: 
                count = 0
                num = i
                while num in seen: 
                    count +=1
                    num+=1
                    max_count = max(max_count, count)
        return max_count


        
                
                    

