class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    q.append((i, j))
                if grid[i][j] == 1: 
                    fresh +=1
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = 0

        while q: 
            if fresh == 0: 
                return minutes
            for _ in range(len(q)):
                y, x = q.popleft()
                for move in moves: 
                    new_y = y + move[0]
                    new_x = x + move[1]
                    if new_y < 0 or new_y >= len(grid) or new_x < 0 or new_x >= len(grid[0]):
                        continue
                    if grid[new_y][new_x] == 1: 
                        grid[new_y][new_x] = 2
                        fresh -=1
                        q.append( (new_y, new_x) )
            minutes +=1
        if fresh == 0: 
            return minutes
        return -1