class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        seen = set()
        for i in prerequisites: 
            graph[i[0]].append(i[1])
        def dfs(node):
            if not node in graph: 
                return True
            seen.add(node)
            for dep in graph[node]:
                if dep in seen: 
                    return False
                print(dep)
                if dfs(dep) == False: 
                    return False
            graph[node] = []
            seen.remove(node) 
        for key in graph: 
            if dfs(key) == False: return False
        return True



            

