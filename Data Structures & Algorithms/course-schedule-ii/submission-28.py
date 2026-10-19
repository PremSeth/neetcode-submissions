class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        indegree = [0] * numCourses
        graph = {}
        for course in range(numCourses):
            graph[course] = []
        for req in prerequisites: 
            graph[req[1]].append(req[0])
            indegree[req[0]] +=1
        q = deque()
        for idx, ind in enumerate(indegree): 
            if ind == 0:
                q.append(idx)
                order.append(idx)
        while q:
            course = q.popleft()
            for depend in graph[course]:
                indegree[depend] -=1
                if indegree[depend] ==0:
                    q.append(depend)
                    order.append(depend)
        if len(order) == numCourses:
            return order
        return []
