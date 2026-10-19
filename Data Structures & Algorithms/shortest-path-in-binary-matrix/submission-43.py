class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set((0, 0))
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        q.append([0, 0, 1])
        while q: 
            print(q)
            x, y, l = q.popleft()
            if x > len(grid)-1 or x < 0 or y > len(grid)-1 or y < 0 or grid[x][y] == 1 or (x, y) in seen: 
                continue
            seen.add((x, y))
            if x == len(grid)-1 and y == len(grid)-1: 
                return l
            else: 
                for move in moves: 
                    new_pos = [a+b for a, b, in zip([x, y], move)]
                    q.append([new_pos[0], new_pos[1], l+1])
        return -1
                    




            
