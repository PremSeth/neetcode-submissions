class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = []
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        seen = set()
        def dfs(node):
            md = 0 
            seen.add(node)
            for connection in graph[node]:
                if connection in seen:
                    continue
                md = max(dfs(connection), md)
            seen.remove(node)
            return 1 + md
        depth_tracker = {}
        for i in range(n):
            depth_tracker[i] = dfs(i)
        min_depth = min(depth_tracker.values())
        res = []
        for key, value in depth_tracker.items():
            if value == min_depth:
                res.append(key)
        return res
