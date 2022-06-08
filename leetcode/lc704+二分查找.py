from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, (len(nums) - 1)
        while left <= right:
            mid = (right - left) // 2 + left
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            elif mid_num > target:
                right = mid - 1
            elif mid_num < target:
                left = mid + 1
        return -1

