class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        length = len(text1)

        dp = [0] * length
        for index, str_item in enumerate(text1):
            if str_item in text2:
                dp[index] = max(dp[:index+1]) + 1
                text2_index = text2.find(str_item)
                text2 = text2[text2_index+1:]
                print(text2)
        return max(dp)


print("abcd".find("b"))
if __name__ == '__main__':
    s = Solution()
    t1 = "bsbininm"
    t2 = "jmjkbkjkv"
    s.longestCommonSubsequence(t1,t2)