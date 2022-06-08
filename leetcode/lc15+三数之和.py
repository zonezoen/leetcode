from typing import List
# https://leetcode-cn.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        length = len(nums)
        right_index = length - 1
        result = []
        for index, num_item in enumerate(nums):
            if num_item > 0:
                break
            if index > 0 and num_item == nums[index - 1]:
                continue
            left = index + 1
            right = right_index
            while left < right:
                if num_item + nums[left] + nums[right] == 0:
                    result.append([num_item, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif num_item + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == '__main__':
    nums = [4, 5, 9, 1, 2, 3, 6]
    nums.sort()
    print(nums)
