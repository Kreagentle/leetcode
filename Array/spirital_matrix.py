class Solution(object):
    def spiralOrder(self, matrix):
        resultList = []
        raw, column = len(matrix), len(matrix[0])
        up = 0
        left = 0
        right = column - 1
        down = raw - 1

        while len(resultList) < raw * column:
                for i in range(left, right + 1):
                        resultList.append(matrix[up][i])
                for i in range(up + 1, down + 1):
                        resultList.append(matrix[i][right])
                if up != down:
                        for i in range(right - 1, left - 1, -1):
                                resultList.append(matrix[down][i])
                if left != right:
                        for i in range(down-1, up, -1):
                                resultList.append(matrix[i][left])
                up += 1
                left += 1
                right -= 1
                down -= 1

        return resultList