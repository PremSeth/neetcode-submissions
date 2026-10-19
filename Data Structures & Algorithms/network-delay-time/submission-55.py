class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {node: [] for edge in times for node in (edge[0], edge[1])}
        
        for i in times: 
            graph[i[0]].append( (i[2], i[1]) )
        
        q = []
        q.append((0, k))
        seen = set()
        while q:
            c1, n1 = heapq.heappop(q)
            if n1 in seen:
                continue
            seen.add(n1)
            if len(seen) == n:
                return c1
            for connect in graph[n1]:
                c2 = connect[0]
                n2 = connect[1]
                if n2 in seen:
                    continue
                heapq.heappush(q, (c2+c1, n2))
        return -1