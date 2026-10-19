class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (-1*math.sqrt( (point[0]*point[0]) + (point[1]*point[1]) ), point) )
            if len(heap) > k: 
                heapq.heappop(heap)
        sol = []
        for i in heap:             
            sol.append(i[1])
        return sol