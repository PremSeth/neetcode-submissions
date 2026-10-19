class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        seen = set()
        for i in times: 
            graph.setdefault(i[0], []).append( (i[2], i[1]) )
        
        q = []
        q.append( (0, k) )
        while q: 
            cost, node = heapq.heappop(q)
            if node in seen:
                continue
            seen.add(node)
            if len(seen) == n: 
                return cost
            if node in graph: 
                for connection in graph[node]:
                    heapq.heappush(q, (cost + connection[0], connection[1]) )
        return -1