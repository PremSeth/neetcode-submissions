class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        found = []
        while left <= right: 
            mid = (left+right)//2
            if target < matrix[mid][0]:
                right = mid-1
            elif target > matrix[mid][-1]: 
                left = mid + 1
            else: 
                found = matrix[mid]
                break
        if found: 
            left = 0
            right = len(found)-1
            while left <= right: 
                mid = (left + right)//2
                if target > found[mid]: 
                    left = mid+1
                elif target < found[mid]: 
                    right = mid-1
                else: 
                    return True
            return False
        else: 
            return False
            