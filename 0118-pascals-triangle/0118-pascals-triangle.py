class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x = []
        for i in range(1, numRows+1):
            y = []
            if i == 1:
                y.append(1)
                x.append(y)
                continue
            if i == 2:
                y.append(1)
                y.append(1)
                x.append(y)
                continue
            if i == 3:
                y.append(1)
                y.append(2)
                y.append(1)
                x.append(y)
                continue

            for j in range(len(x[i-2])):
                if j == 0:
                    y.append(1)
                if j == len(x[i - 2]) - 1:
                    y.append(1)
                else:
                    y.append(x[i-2][j] + x[i - 2][j + 1])
            x.append(y)

        return x

        