class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_checker = defaultdict(set)
        col_checker = defaultdict(set)
        square_checker = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.': 
                    continue
                if num in row_checker[i] or num in col_checker[j] or num in square_checker[i//3, j//3]:
                    return False
                else: 
                    row_checker[i].add(num)
                    col_checker[j].add(num)
                    square_checker[i//3, j//3].add(num)
                    print(row_checker.items())
        return True


                
