class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        seen = {}
        def dfs(y, x):
            if y < 0 or x < 0 or y > m-1 or x > n-1:
                return 0
            if (y, x) in seen:
                return seen[ (y, x) ]
            if y == m-1 and x == n-1: 
                return 1
            val = dfs(y+1, x) + dfs(y, x+1)
            seen[ (y, x) ] = val
            return val 
        return dfs(0, 0)