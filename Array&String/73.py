class Solution(object):
    def setZeroes(self, matrix):
        n, m = len(matrix), len(matrix[0])
        zeroinFirstCol = False
        zeroinFirstRow = False

        for row in range(n):
            if matrix[row][0] == 0:
                zeroinFirstCol = True
                break

        for col in range(m):
            if matrix[0][col] == 0:
                zeroinFirstRow = True
                break

        for row in range(1, n):
            for col in range(1, m):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, n):
            for col in range(1, m):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if zeroinFirstCol:
            for row in range(0, n):
                matrix[row][0] = 0

        if zeroinFirstRow:
            for col in range(0, m):
                matrix[0][col] = 0
