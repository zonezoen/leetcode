class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        left = 0
        result = ""
        for right, sub_str, in enumerate(s):
            left_str = ""
            right_str = ""
            mid_str = ""
            while left < right:
                if s[left] == s[right]:
                    if left + 1 == right - 1:
                        left_str = left_str + s[left]
                        right_str = s[right] + right_str
                        mid_str = s[left + 1]
                        break
                    else:
                        left_str = left_str + s[left]
                        right_str = s[right] + right_str
                    right -= 1
                if left_str and s[left] != s[right]:
                    left_str = ""
                    right_str = ""
                    mid_str = ""
                left += 1
            result_str = left_str + mid_str + right_str
            if len(result_str) > len(result):
                result = result_str
            left = 0
        return result if result else result[0]
