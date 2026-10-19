class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        spoil = set()
        fruit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    fruit.add((i, j))
                if grid[i][j] == 2: 
                    q.append((i, j))
                    spoil.add((i, j))
        start = len(spoil)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        while q:
            for i in range(len(q)): 
                pos = q.popleft()
                grid[pos[0]][pos[1]] = 2
                print(minutes)
                for move in moves: 
                    new_pos = (move[0] + pos[0], move[1] + pos[1])
                    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > len(grid)-1 or new_pos[1] > len(grid[0])-1 or new_pos in spoil or grid[new_pos[0]][new_pos[1]] == 0: 
                        continue
                    spoil.add(new_pos)
                    q.append(new_pos)
            minutes+=1 
        if len(fruit) == 0:
            return 0
        if len(spoil)-start == len(fruit): 
            return minutes-1
        else: 
            return -1