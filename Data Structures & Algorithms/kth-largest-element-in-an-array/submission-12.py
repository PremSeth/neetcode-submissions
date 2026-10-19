class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums: 
            heapq.heappush(heap, -i)
            if len(heap) > len(nums)-k+1:
                heapq.heappop(heap)
        return -1*heapq.heappop(heap) 