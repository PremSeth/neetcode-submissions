class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append( (sr, sc) )
        color1 = image[sr][sc]
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        seen.add((sr, sc))
        while q: 
            for i in range(len(q)): 
                pos = q.pop()
                x = pos[0]
                y = pos[1]
                print(x, y)
                image[x][y] = color
                for move in moves: 
                    new_move = (x + move[0], y + move[1])
                    if new_move[0] < 0 or new_move[1] < 0 or new_move[0] > len(image)-1 or new_move[1] > len(image[0])-1 or new_move in seen: 
                        continue
                    print(new_move[0], new_move[1])
                    if image[new_move[0]][new_move[1]] == color1: 
                        q.append(new_move)
                        seen.add(new_move)
        return image
