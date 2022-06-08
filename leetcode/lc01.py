from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        for index_i,item_i, in enumerate(nums):
            for index_j,item_j, in enumerate(nums):
                if index_i == index_j:
                    continue
                if nums[index_i] + nums[index_j] == target:
                    return [index_i,index_j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for index, num in enumerate(nums):
            if target - num  not in myDict:
                myDict[num] = index
            else:
                print([myDict[target - num], index])
                return [myDict[target - num], index]
# class Solution3:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         myDic = {}
#         for index, num in enumerate(nums):
#             myDic[num] = index
#         for index, num in enumerate(nums):
#             if target - num not in myDic and :
#                 print([index,myDic[target - num]])
#                 return [index,myDic[target - num]]


if __name__ == '__main__':
    s = Solution3()
    s.twoSum([3,3]
,6)