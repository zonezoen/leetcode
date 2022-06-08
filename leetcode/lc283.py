from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index_list = []
        for index,num in enumerate(nums):
            if num == 0:
                zero_index_list.append(index)
        print(zero_index_list)
        length = len(zero_index_list)
        for list_item in reversed(zero_index_list):
            nums.pop(list_item)
        for _ in range(length):
            nums.append(0)

if __name__ == '__main__':
    for item in reversed([1,2,3]):
        print(item)