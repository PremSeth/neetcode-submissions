class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        graph = {}
        for i in range(numCourses): 
            graph[i] = []
        for i in prerequisites: 
            graph[i[1]].append(i[0])
            indegree[i[0]] +=1
        order = [0]*numCourses
        index = 0
        q = deque()
        for i,j in enumerate(indegree): 
            if j == 0:
                q.append(i)
                order[index] = i
                index +=1

        while q: 
            course = q.popleft()
            for blocked in graph[course]:
                indegree[blocked] -=1
                if indegree[blocked] == 0: 
                    q.append(blocked)
                    order[index] = blocked
                    index +=1
        if index == numCourses: 
            return order
        return []

            