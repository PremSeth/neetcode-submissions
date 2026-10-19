class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) * len(matrix[0])-1
        while left<=right: 
            mid = (left+right)//2
            row = mid // len(matrix[0]) 
            idx = mid % len(matrix[0])
            guess= matrix[row][idx]
            print(left, right, row, idx)
            if guess > target: 
                right = mid-1
            elif guess < target: 
                left = mid + 1
            else: 
                return True
        return False

        