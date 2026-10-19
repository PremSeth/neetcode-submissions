class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        seen = {}
        def dfs(y, x):
            if y< 0 or x < 0 or y > len(grid)-1 or x > len(grid[0])-1:
                return float("inf")
            if y == len(grid)-1 and x == len(grid[0])-1:
                return grid[y][x]
            if (y, x) in seen:
                return seen[(y, x)]
            cheapest = min(dfs(y+1, x), dfs(y, x+1))
            seen[(y, x)] = cheapest + grid[y][x]
            return cheapest + grid[y][x]
        return dfs(0, 0)