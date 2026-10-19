class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums: 
            counts[i] +=1
        clean = sorted(counts.items(), key = lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(clean[i][0])
        return res