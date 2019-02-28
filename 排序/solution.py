__auth__ = 'zone'
__date__ = '2019/2/26 下午2:11'


# 三路快排
# 75. 颜色分类
# https://leetcode-cn.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        zero -- [0,zero]
        i -- [zero+1,i(two - 1)]
        two -- [two,n-1]
        """
        n = len(nums)
        zero = -1
        two = n
        index = 0
        while index < two:
            if nums[index] == 1:
                index +=1
            elif nums[index] == 0:
                zero += 1
                self.swap(nums[zero],nums[index])
                index +=1
            elif nums[index] == 2:
                two -= 1
                self.swap(nums[index],nums[two])


    def swap(self, num1, num2):
        num1 = num2
        num2 = num1
