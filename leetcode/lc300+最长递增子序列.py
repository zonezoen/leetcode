from typing import List
# https://leetcode.cn/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length # dp[i] 表示当前 i 位置的最大子序列长度
        # 转移方程：dp[i] = max(dp[i],dp[0~i-1] + 1)
        for right, num_item in enumerate(nums):
            for left in range(right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], dp[left] + 1)
        return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        my_dict = {}
        for index, num_item in enumerate(nums):
            max_val = 0  # 记录小于当前值 key 的最长子序列长度
            for key, val in my_dict.items():
                if num_item > key:
                    if val > max_val:
                        max_val = val
            # 如果等于 0，则说明在 num_item 之前没有小于 num_item 的数据
            if max_val == 0:
                my_dict[num_item] = 1
            else:
                my_dict[num_item] = max_val + 1
        return max(my_dict.values())

    def lengthOfLIS(self, nums: List[int]) -> int:
        my_dict = {}
        max_result = 0
        for index, num_item in enumerate(nums):
            max_val = 0  # 记录小于当前值 key 的最长子序列长度
            for key, val in my_dict.items():
                if num_item > key:
                    if val > max_val:
                        max_val = val
            # 如果等于 0，则说明在 num_item 之前没有小于 num_item 的数据
            if max_val == 0:
                my_dict[num_item] = 1
            else:
                my_dict[num_item] = max_val + 1
            max_result = max(max_result,my_dict.get(num_item))
        return max_result
