class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i+1 for i in range(n)]
        rank = [1]*n

        def find(n1):
            par = parents[n1-1]
            if par != n1:
                parents[n1-1] = find(par)
            return parents[n1-1]
        redundant = 0
        def union(edge):
            n1 = edge[0]
            n2 = edge[1]
            p1 = find(n1)
            p2 = find(n2)
            
            nonlocal redundant
            if p1 == p2: 
                print('active')
                redundant = edge
            
            if rank[p1-1] < rank[p2-1]:
                parents[p1-1] = p2
                rank[p2-1] += rank[p1-1]
                rank[p1-1] = 0
            else:
                parents[p2-1] = p1
                rank[p1-1] += rank[p2-1]
                rank[p2-1] = 0
            return redundant
        for edge in edges: 
            union(edge)
        return redundant