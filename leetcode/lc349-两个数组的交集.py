# https://leetcode-cn.com/problems/intersection-of-two-arrays/
#

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            return self.child_inter(nums1, nums2)
        else:
            return self.child_inter(nums2, nums1)

    def child_inter(self, nums1: List[int], nums2: List[int]):
        result = set()
        for num in nums1:
            if num in nums2:
                result.add(num)
        return list(result)
