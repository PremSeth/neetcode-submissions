class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] =1
        total = 0
        subarrays = 0
        for i in nums: 
            total +=i
            subarrays += prefix_sums.get(total-k, 0)
            prefix_sums[total] +=1
        return subarrays


            
        