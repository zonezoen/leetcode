from typing import List


def partition(nums: List, left, right):
    # print(nums)
    # print(left)
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
        quicksort(nums, left, index - 1)
        quicksort(nums, index + 1, right)


def split_k(nums: List, k, left, right):
    if left < right:
        index = partition(nums, left, right)
        if index == k:
            return
        elif index < k:
            split_k(nums, k, index + 1, right)
        else:
            split_k(nums, k, left, index - 1)

def topk_split(nums, k, left, right):
    # 寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    if (left < right):
        index = partition(nums, left, right)
        if index == k:
            return
        elif index < k:
            topk_split(nums, k, index + 1, right)
        else:
            topk_split(nums, k, left, index - 1)


if __name__ == '__main__':
    nums = [5, 1, 2, 6, 5, 9, 3]
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    nums = [3, 2, 1, 5, 6, 4]
    nums = [-1,2,0]

    k = 2
    length = len(nums)
    print(nums)
    # quicksort(nums, 0, len(nums) - 1)

    split_k(nums, length - 1 - k, 0, length - 1)
    # topk_split(nums, length - 1 - k, 0, length - 1)
    print(nums)
    print(nums[0 - k])
