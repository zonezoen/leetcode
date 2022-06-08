from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == "1":
                    self.dfs(grid, row, column)
                    result += 1
        return result

    def dfs(self, grid: List[List[str]], row: int, column):
        # 处理越界问题
        if row < 0 or column < 0 or row > len(grid) - 1 or column > len(grid[0]):
            return
        # 如果是“0”、“2”，则直接返回
        if grid[row][column] != "1":
            return
        # 如果是“1”，就改为“2”，表示已经扫描过的陆地
        grid[row][column] = "2"

        self.dfs(grid, row - 1, column)
        self.dfs(grid, row, column - 1)
        self.dfs(grid, row + 1, column)
        self.dfs(grid, row, column + 1)
