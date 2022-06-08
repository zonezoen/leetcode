from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:


    def dfs(self, grid: List[List[int]], row: int, column: int, last_sum: int, result: List):
        tmp_sum = grid[row][column] + last_sum
        if row == self.row_length - 1 and column < self.column_length - 1:
            self.dfs(grid, row, column + 1, tmp_sum, result)
        if column == self.column_length - 1 and row < self.row_length - 1:
            self.dfs(grid, row + 1, column, tmp_sum, result)
        if row < self.row_length - 1:
            self.dfs(grid, row + 1, column, tmp_sum, result)
        if column < self.column_length - 1:
            self.dfs(grid, row, column + 1, tmp_sum, result)

        if row == self.row_length - 1 and column == self.column_length - 1:
            result.append(tmp_sum)
        # if row + 1 < self.row_length and column + 1 < self.column_length:
        #     self.dfs(grid, row + 1, column, tmp_sum, result)
        #     self.dfs(grid, row, column + 1, tmp_sum, result)


print(min([1, 2, 3]))
