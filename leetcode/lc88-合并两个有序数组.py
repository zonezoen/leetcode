from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        result = []
        while p1 < m or p2 < n:
            if p1 == m:
                result.append(nums2[p2])
                p2 += 1
                continue
            if p2 == n:
                result.append(nums1[p1])
                p1 += 1
                continue
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        nums1[:] = result
