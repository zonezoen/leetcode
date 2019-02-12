# 26. 删除排序数组中的重复项
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
class Solution:
# 重新生成了 list，地址改变了，导致原数组没有得到改变
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        print(nums)
        return len(nums)

# 26.88% 128ms
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        print(my_dict)
        for index, key in enumerate(my_dict.keys()):
            nums[index] = key
        return len(my_dict)

# 网络上的最优解
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        '''这个版本，占内存少，但是耗时'''
        # pointer = 0
        # for i in range(len(nums)):
        #     if nums[i]==nums[pointer]:
        #         continue
        #     pointer += 1
        #     nums[pointer] = nums[i]
        # return pointer+1

        '''这个版本，占内存多，但是省时间'''
        pointer = 1  # 指向下一个要存放非重复数的位置
        num_dup = nums[0]  # 存放重复数字
        for i in range(len(nums)):
            if nums[i] == num_dup:
                continue
            nums[pointer] = nums[i]
            num_dup = nums[i]
            pointer += 1
        return pointer


s = Solution()
nums = [1, 1, 2]
s.removeDuplicates(nums)
print(nums)
