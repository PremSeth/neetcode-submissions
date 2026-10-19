class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        indegree = [0] * numCourses
        graph = {}
        pre_req = {}
        for course in range(numCourses):
            graph[course] = []
            pre_req[course] = []
        for req in prerequisites: 
            graph[req[1]].append(req[0])
            pre_req[req[0]].append(req[1])
            indegree[req[0]] +=1
        q = deque()
        for course in pre_req: 
            if not pre_req[course]:
                q.append(course)
                order.append(course)
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
