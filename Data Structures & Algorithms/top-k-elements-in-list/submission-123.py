class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums: 
            freq[i] = freq.get(i, 0) + 1
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (val, key) )
            if len(heap) > k: 
                heapq.heappop(heap)
        most_freq = []
        for i in range(k):
            most_freq.append(heapq.heappop(heap)[1])
        return most_freq
