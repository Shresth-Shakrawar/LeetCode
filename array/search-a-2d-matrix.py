class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top , bot = 0 , ROWS - 1 # top and bottom row pointers
        while top<= bot:
            row = (top+bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if top > bot:
            return False
    
        mid_row = (top+bot) // 2
        l , r = 0,COLS-1
        while l<=r:
            mid = (l+r) // 2
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True
                
        return False
