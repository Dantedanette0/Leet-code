class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        row = 0

        for i in range(rows):
            if target >= matrix[i][0]:
                row = i
        
        if target in matrix[row]:
            return True
        
        return False

        