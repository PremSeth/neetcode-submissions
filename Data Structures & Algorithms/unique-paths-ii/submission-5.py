class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        seen = {}
        def dfs(y, x):
            if (y, x) in seen:
                return seen[(y, x)]
            
            if y < 0 or x < 0 or y > len(obstacleGrid)-1 or x > len(obstacleGrid[0]) -1 or obstacleGrid[y][x] == 1:
                seen[ (y, x) ] = 0 
                return 0
            if y == len(obstacleGrid)-1 and x == len(obstacleGrid[0])-1: 
                return 1
            val = dfs(y+1, x) + dfs(y, x+1)
            seen[(y, x)] = val
            return val
        return dfs(0, 0)