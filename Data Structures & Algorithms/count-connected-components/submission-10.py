class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            par = parents[n1]
            if par != n1:
                parents[n1] = find(par)
            return parents[par]
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2: 
                return 0
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] +=1
            else:
                parents[p1] =p2
                rank[p2] +=1
            return 1
        for edge in edges: 
            n-= union(edge[0], edge[1])
        return n