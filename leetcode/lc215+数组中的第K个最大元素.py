from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.split_k(nums,k,0,len(nums)-1)
        return nums[0 - k]

    def partition(self, nums: List, left, right):
        pivot = nums[left]

        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]

            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    def split_k(self, nums: List, k, left, right):
        if left < right:
            index = self.partition(nums, left, right)
            if index == k:
                return
            elif index < k:
                self.split_k(nums, k, index + 1, right)
            else:
                self.split_k(nums, k, left, index - 1)
