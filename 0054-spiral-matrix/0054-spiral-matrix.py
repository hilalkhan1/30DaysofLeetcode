class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        row_start = 0
        row_end = rows - 1
        col_start = 0
        col_end = cols - 1

        while row_start <= row_end and col_start <= col_end:
            # Traverse right
            for col in range(col_start, col_end+1):
                result.append(matrix[row_start][col])
            row_start += 1

            # Traverse down
            for row in range(row_start, row_end+1):
                result.append(matrix[row][col_end])
            col_end -=1

            # Traverse left
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][col])
                row_end -= 1
            
            # Traverse up
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    result.append(matrix[row][col_start])
                col_start += 1
        return result
