class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def isValue(pair): 
            if pair in seen: 
                return False
            if pair[0] < 0 or pair[1] < 0 or pair[0] > len(grid[0])-1 or pair[1] > len(grid)-1: 
                return False
            if grid[pair[1]][pair[0]] ==1: 
                seen.add(pair)
                return True
        def dfs(pair): 
            connections = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            count = 1
            for i in connections: 
                new_pair = (pair[0]+i[0], pair[1]+i[1])
                if isValue(new_pair):
                    count += dfs(new_pair)
            return count
        area = 0
        for y in range(len(grid)): 
            for x in range(len(grid[0])):
                pair = (x, y)
                if isValue(pair): 
                    area = max(dfs(pair), area)
        return area
