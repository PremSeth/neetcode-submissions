class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        def dfs(node):
            y = node[0]
            x = node[1]
            moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for move in moves: 
                new_y = y + move[0]
                new_x = x + move[1]
                if (new_y, new_x) in seen:
                    continue
                if new_y < 0 or new_x < 0 or new_y >= len(grid) or new_x >= len(grid[0]): 
                    continue
                if grid[new_y][new_x] == '1':
                    seen.add( (new_y, new_x) )
                    dfs( (new_y, new_x) )
            return 
        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not (i, j) in seen: 
                    dfs( (i, j) )
                    island_count +=1
        return island_count