class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        graph = {}
        for i in range(n):
            graph[i+1] = []
        
        seen = set()
        for i in times:
            graph[i[0]].append( (i[2], i[1]) )
        heap.append((0, k))
        while heap: 
            cost, pos = heapq.heappop(heap)
            if pos in seen:
                continue
            seen.add(pos)
            if len(seen) == n:
                return cost
            for time, node in graph[pos]:

                heapq.heappush(heap, ( (cost+time), node))
            
        return -1