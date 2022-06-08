from typing import List, Optional


class Solution:
    def compress(self, chars: List[str]) -> int:
        my_dict = {}
        for char in chars:
            my_dict[char] = my_dict.get(char, 0) + 1
        result = 0
        chars.clear()
        for key, val in my_dict.items():
            if val == 1:
                result += 1
                chars.append(key)
            else:
                chars.append(key)
                for item in str(val):
                    chars.append(item)
                result += 1
                result += len(str(val))
        return result
