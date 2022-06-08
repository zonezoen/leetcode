from typing import List


def partition(nums: List, left, right):
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


def quicksort(nums: List, left, right):
    if left < right:

        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index + 1, right)


if __name__ == '__main__':
    nums = [5, 2, 6, 9, 3, 6]
    quicksort(nums, 0, len(nums)-1)
    print(nums)


