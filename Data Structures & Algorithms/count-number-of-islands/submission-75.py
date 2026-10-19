class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = set()
        def isValid(pair):
            if pair in seen:
                return False
            if pair[0] < len(grid) and pair[1] < len(grid[0]) and pair[0] >= 0 and pair[1] >= 0:     
                if grid[pair[0]][pair[1]] == '1': 
                    seen.add(pair)
                    return True
            return False
        def dfs(pair):
            moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for move in moves: 
                new_move = (pair[0] + move[0], pair[1] + move[1])
                if isValid(new_move):
                    dfs(new_move)
        
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                    if isValid( (i, j) ):
                        count +=1
                        dfs( (i, j) )
        return count
