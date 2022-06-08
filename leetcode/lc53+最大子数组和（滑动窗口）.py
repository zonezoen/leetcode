# https://leetcode-cn.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        my_dict = {}
        max_sum = -10 ^ 4
        for index, num_item in enumerate(nums):
            if index == 0:
                my_dict[index] = num_item
                max_sum = max(max_sum, num_item)
            else:
                if my_dict[index - 1] > 0:
                    my_dict[index] = num_item + my_dict[index - 1]
                    max_sum = max(max_sum, my_dict[index])
                else:
                    my_dict[index] = num_item
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        dp = {}
        max_result = -10001
        for index, num_item in enumerate(nums):
            if not dp:
                dp[index] = num_item
                max_result = max(max_result, dp[index])
            else:
                if dp[index - 1] > 0:
                    dp[index] = dp[index - 1] + nums[index]
                    max_result = max(max_result, dp[index])
                else:
                    dp[index] = nums[index]
                    max_result = max(max_result, dp[index])
        return max_result

    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0 for _ in length]
        dp[0] = nums[0]
        max_result = dp[0]
        for index in range(1,length):
            if dp[index-1] > 0:
                dp[index] = dp[index - 1] + nums[index]
                max_result = max(max_result, dp[index])
            else:
                dp[index] = nums[index]
                max_result = max(max_result, dp[index])
        return max_result