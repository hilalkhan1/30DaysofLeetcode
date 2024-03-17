class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x = [[1], [1, 1], [1, 2, 1]]
        if numRows == 1:
            return [x[0]]
        if numRows == 2:
            return [x[0:2]]
        if numRows == 3:
            return x

        for i in range(4, numRows+1):
            y = []
            for j in range(len(x[i-2])):
                if j == 0:
                    y.append(1)
                if j == len(x[i - 2]) - 1:
                    y.append(1)
                else:
                    y.append(x[i-2][j] + x[i - 2][j + 1])
            x.append(y)

        return x

        