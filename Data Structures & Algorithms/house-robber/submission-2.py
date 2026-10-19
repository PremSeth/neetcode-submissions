class Solution:
    def rob(self, nums: List[int]) -> int:
        l_max = 0
        r_max = 0
        curr = 0
        for i in nums: 
            curr = max(i+l_max, r_max)
            l_max = r_max
            r_max = curr
        return curr
