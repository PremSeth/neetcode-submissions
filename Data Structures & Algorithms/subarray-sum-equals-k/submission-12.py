class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {}
        prefixes[0] = 1
        ways = 0
        running = 0
        for i in nums: 
            running +=i 
            ways += prefixes.get(running-k, 0)
            print(running)
            prefixes[running] = prefixes.get(running, 0) + 1
        return ways