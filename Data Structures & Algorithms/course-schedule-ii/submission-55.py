class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        graph = {}

        for i in range(numCourses):
            graph[i] = []

        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] +=1
        order = []
        q = deque()
        for i,j in enumerate(indegree): 
            if j == 0: 
                q.append(i)
        while q: 
            course = q.popleft()
            order.append(course)
            if len(order) == numCourses:
                return order
            for depend in graph[course]:
                indegree[depend]-=1
                if indegree[depend] ==0: 
                    q.append(depend)
        return []
