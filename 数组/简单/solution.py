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


# s = Solution()
# nums = [1, 1, 2]
# s.removeDuplicates(nums)
# print(nums)


# 27. 移除元素
# https://leetcode-cn.com/problems/remove-element/
class Solution:
    # 76.98% 48ms
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return 0
        nums_length = len(nums)
        for index, num in enumerate(reversed(nums)):
            if num == val:
                nums.pop(nums_length - index - 1)
        return len(nums)

    # 76.98 48ms
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return 0
        value_index = []
        for index, num in enumerate(nums):
            if num == val:
                value_index.append(index)
        for index in reversed(value_index):
            nums.pop(index)
        return len(nums)

# 网络最优解
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return 0
        pointer = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[pointer] = nums[i]
            pointer += 1
        return pointer

def run27():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    s = Solution()
    s.removeElement(nums, 2)
    print(nums)


# 35. 搜索插入位置
# https://leetcode-cn.com/problems/search-insert-position/
class Solution:
# 99.56% 44ms
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        result = len(nums)
        for index,num in enumerate(nums):
            if num == target:
                print(f'num{num} = target{target} , index is {index}')
                result = index
                break
            if num > target:
                print(f'num{num} > target{target} , index is {index}')
                result = index
                break
        while target not in nums:
            print(f'insert num{target} on {index}')
            nums.insert(result, target)
        return result

# 网络最优解
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
def run35():
    nums = [1,3,5,6]
    s = Solution()
    s.searchInsert(nums, 7)
    print(nums)
run35()