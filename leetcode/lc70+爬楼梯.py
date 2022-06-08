# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    result_dict = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = None
        if n in self.result_dict:
            result = self.result_dict.get(n)
        else:
            result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.result_dict[n] = result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
