# https://leetcode-cn.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_nums_length = len(nums) / 2
        result_dict = {}
        for num_item in nums:
            result_dict[num_item] = result_dict.get(num_item, 0) + 1
            if result_dict.get(num_item) > half_nums_length:
                return num_item
