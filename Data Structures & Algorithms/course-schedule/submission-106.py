class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for i in prerequisites: 
            graph[i[0]].append(i[1])
        print(graph)
        seen = set()
        def dfs(node): 
            print(node)
            if node in seen: 
                return False
            
            if node == []: 
                return True
            
            seen.add(node)

            for course in graph[node]: 
                if not dfs(course): 
                    return False
            
            seen.remove(node)
            graph[node] = []
            return True
        
        for i in range(numCourses): 
            if not dfs(i):
                return False
        return True