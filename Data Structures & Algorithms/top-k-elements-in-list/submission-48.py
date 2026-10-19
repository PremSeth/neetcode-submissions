class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums: 
            seen[i] = seen.get(i, 0) + 1
        return sorted(seen, key=lambda a: -seen[a])[:k]