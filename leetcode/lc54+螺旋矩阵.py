# https://leetcode-cn.com/problems/spiral-matrix/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1
        result = []
        while True:
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):
                result.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left - 1, -1):
                result.append(matrix[down][i])
            down -= 1
            if up > down:
                break
            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return result
        print(result)


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.spiralOrder(matrix)
