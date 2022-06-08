# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        none_result = [-1, -1]
        if not nums:
            return none_result
        result = []
        for index, num in enumerate(nums):
            if num == target:
                result.append(index)
        if len(result) > 1:
            return [result[0], result[-1]]
        else:
            return none_result
