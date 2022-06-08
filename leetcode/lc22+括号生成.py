from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.left_count = n
        self.right_count = n
        result = []
        self.my_list = ["("] * n + [")"] * n
        self.used = [False] * n * 2
        self.dfs(n, [], result, 0, 0)
        return result

    def dfs(self, n: int, path: List, result: List, left_size: int, right_size: int):
        if len(path) == n * 2:
            tmp_ret = "".join(path)
            if tmp_ret not in result:
                result.append(tmp_ret)
            return

        for index in range(n * 2):

            if not self.used[index] and left_size >= right_size:
                tmp_ret = self.my_list[index]
                if tmp_ret == "(":
                    left_size += 1

                else:
                    right_size += 1
                self.used[index] = True
                path.append(tmp_ret)
                self.dfs(n, path, result, left_size, right_size)
                path.pop()
                self.used[index] = False
                if tmp_ret == "(":
                    left_size -= 1

                else:
                    right_size -= 1


if __name__ == '__main__':
    print(["("] * 3 + [")"] * 3)
