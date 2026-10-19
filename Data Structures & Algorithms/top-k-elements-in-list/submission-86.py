class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums: 
            counts[i] = counts.get(i, 0) - 1
        top_freq = [(k, j) for j, k in counts.items()]
        heapq.heapify(top_freq)
        most_frequent = []
        for i in range(k): 
            most_frequent.append(heapq.heappop(top_freq)[1])
        return most_frequent