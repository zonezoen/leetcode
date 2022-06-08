from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(1 ,len(nums)+1):
            if index not in nums:
                return index
        return len(nums) + 1