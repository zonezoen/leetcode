# https://leetcode-cn.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.size = len(nums)
        self.used = [False * i for i in range(self.size)]
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums: List, depth: int, path: List, result: List):
        # 停止遍历条件
        if depth == self.size:
            result.append(path[:])

        for index in range(self.size):
            if self.used[index] is False:
                self.used[index] = True
                path.append(nums[index])

                self.dfs(nums, depth + 1, path, result)

                self.used[index] = False
                path.pop()


if __name__ == '__main__':
    ret = [True for i in range(4)]
    print(ret)
