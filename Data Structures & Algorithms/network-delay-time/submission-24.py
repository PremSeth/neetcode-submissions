class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for i in times: 
            graph[i[0]].append((i[2], i[1]))
        heap = [(0, k)]
        heapq.heapify(heap)
        seen = set()
        time = 0
        print(graph)
        while heap: 
            weight, node = heapq.heappop(heap)
            if node in seen: 
                continue
            seen.add(node)
            time = max(time, weight)
            if node in graph: 
                for w, n1 in graph[node]: 
                    heapq.heappush(heap, (weight + w, n1))
            print(heap)
        print(len(seen))
        print(n)
        if len(seen) < n: 
            return -1
        return time


