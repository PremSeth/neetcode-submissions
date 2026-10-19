class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in prerequisites: 
            graph[i[0]].append(i[1])
        seen = set()
        def dfs(node):
            if node in seen: 
                return False
            if node in graph: 
                seen.add(node)
                for dep in graph[node]: 
                    if not dfs(dep):
                        return False
                seen.remove(node)
                graph[node] = []
                return True
            else: 
                return True
        for dep in graph: 
            if not dfs(dep): 
                return False
        return True
