class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def isValid( pair ):
            if pair in seen: 
                return False
            y = pair[0]
            x = pair[1]
            if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
                if grid[y][x] == 1: 
                    seen.add(pair)
                    return True
            return False
        
        def dfs( pair ):
            moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            if isValid(pair):
                y = pair[0]
                x = pair[1]
                count = 1
                for move in moves: 
                    y_new = move[0] + y
                    x_new = move[1] + x
                    count += dfs( (y_new, x_new) )
                return count
            return 0
        best_area = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                pair = (y, x)
                best_area = max(best_area, dfs(pair))
        return best_area
                
                