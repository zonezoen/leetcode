from typing import List, Optional
# 代码随想录 PDF 的题解

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        self.backtracing(k, n, path, result, 1)
        return result

    def backtracing(self, k, n, path: List, result: List, start_index):
        if len(path) == k:
            if sum(path) == n:
                result.append(path[:])
            return
        # for index in range(start_index, 10-(k-len(path))+1):
        for index in range(start_index, 11 - (k - len(path))):
            path.append(index)
            self.backtracing(k, n, path, result, index + 1)
            path.pop()


if __name__ == '__main__':
    k = 3
    n = 7
    s = Solution()
    print(s.combinationSum3(k, n))
