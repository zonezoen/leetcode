from typing import List
# https://leetcode-cn.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        myDict = {}
        for num in nums:
            myDict[num] = myDict.get(num,0) + 1
        for key,val in myDict.items():
            if val == 1:
                return key
