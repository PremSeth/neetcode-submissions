class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        def isValid(pair): 
            if pair in seen: 
                return False
            if pair[0] < 0 or pair[1] < 0: 
                return False
            if pair[0] > len(grid[0])-1 or pair[1] > len(grid)-1: 
                return False
            if grid[pair[1]][pair[0]] == '0': 
                return False
            seen.add(pair)
            return True
        count = 0
        def dfs(pair): 
            translations = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            for i in translations:
                new = (pair[0]+i[0], pair[1]+i[1])
                if isValid(new): 
                    dfs(new)
        
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                pair = (j, i)
                if isValid(pair): 
                    dfs((j, i))
                    count +=1
        return count
        