class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros_index.append((i, j))

        for index in zeros_index:
            i, j = index
            for k in range(len(matrix[i])):
                matrix[i][k] = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0

        