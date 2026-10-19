class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums: 
            freq[i] +=1
        return sorted(set(nums), key = lambda x: -freq[x])[0:k]

