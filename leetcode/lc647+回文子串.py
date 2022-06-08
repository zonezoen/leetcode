class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        for right, str_item in enumerate(s):
            for left in range(right):
                if right - left == 1:
                    dp[left][right] = True
                elif right - left > 1:
                    if s[left] != s[right]:
                        dp[left][right] = False
                    else:
                        dp[left][right] = dp[left + 1][right - 1]
                if dp[left][right]:
                    result += 1
        return result
