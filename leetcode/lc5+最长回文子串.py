# https://leetcode.cn/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/

class Solution:
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            length = len(s)
            if length < 2:
                return s
            begin = 0
            max_length = 1

            dp = [[False] * length for _ in range(length)]
            # dp[i][j] 表示字符串位置 i-j 是不是回文字符串，默认为 False

            # 默认 i < j,且 dp[i][i] 是指单个字符串，但个字符串认为是回文串
            for i in range(length):
                dp[i][i] = True

            for right in range(length):
                for left in range(right):
                    if s[left] != s[right]: # 如果首和尾都不相等，那么这个区间的字符串就不会是回文串
                        dp[left][right] = False
                    else: # 如果首和尾相等
                        if right - left < 3: # 处理  aa，aba 这种问题
                            dp[left][right] = True
                        else:
                            dp[left][right] = dp[left + 1][right - 1]
                    if dp[left][right] == True and (right - left + 1) > max_length:
                        begin = left
                        max_length = right - left + 1
            return s[begin:begin + max_length]


    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s
        begin = 0
        max_length = 1

        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True

        for right in range(length):
            for left in range(right):
                if s[left] != s[right]:
                    dp[left][right] = False
                else:
                    if right - left < 3:
                        dp[left][right] = True
                    else:
                        dp[left][right] = dp[left + 1][right - 1]
                if dp[left][right] == True and (right - left + 1) > max_length:
                    begin = left
                    max_length = right - left + 1
        return s[begin:begin + max_length]


# length = 4
# dp = [[False] * length for _ in range(length)]
# for i in range(length):
#     dp[i][i] = True
# print(dp)
s = "abcdefghij"
print(s[1:3])