class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        degree = {}
        for i in range(n):
            graph[i] = []
        
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
            degree[n1] = degree.get(n1, 0) + 1
            degree[n2] = degree.get(n2, 0) + 1
        
        q = deque()
        for key, val in degree.items(): 
            if val == 1:
                q.append(key)
        
        while q: 
            if n <= 2: 
                return list(q)
            for _ in range(len(q)):
                node = q.popleft()
                n-=1
                for nei in graph[node]:
                    degree[nei] -=1
                    if degree[nei] == 1: 
                        q.append(nei)
        return [0]
