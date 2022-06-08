from typing import List, Optional
class

class Solution:
    my_dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        ans_length = len(digits)
        path = []
        result = []
        self.backtracing(ans_length, path, result, digits, 0)
        return result

    def backtracing(self, ans_length, path: List, result: List,
                    digits: str, i_start: int):
        if i_start == ans_length-1:
            result.append("".join(path[:]))
            print(path)
            return

        str_index = digits[i_start]
        tmp_str = self.my_dict[str_index]

        for i in range(len(tmp_str)):
            path.append(tmp_str[i])
            self.backtracing(ans_length, path, result, digits, i + 1)
            path.pop()

if __name__ == '__main__':
    digits = "23"
    s = Solution()
    print(s.letterCombinations(digits))