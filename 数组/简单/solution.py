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


# run27()


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
        if len(nums) == 0:
            return 0
        result = len(nums)
        for index, num in enumerate(nums):
            if num == target:
                # print(f'num{num} = target{target} , index is {index}')
                result = index
                break
            if num > target:
                # print(f'num{num} > target{target} , index is {index}')
                result = index
                break
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
    nums = [1, 3, 5, 6]
    s = Solution()
    s.searchInsert(nums, 7)
    print(nums)


# run35()


# 53. 最大子序和
# https://leetcode-cn.com/problems/maximum-subarray/
class Solution:
    # 耗时太长了，不通过
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = - 2 ** 31
        for i in range(len(nums)):
            index = i + 1

            while index <= len(nums):
                # my_dict[str(i) + str(index)] = sum(nums[i:index])
                if sum(nums[i:index]) > result:
                    result = sum(nums[i:index])
                index += 1
        return result

    # 动态规划
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp, max = 0, -2 ** 31

        for index, num in enumerate(nums):
            if temp < 0:
                temp = 0
            temp += num
            max = max(max, temp)
        return max


def run57():
    nums = [-1]
    s = Solution()
    result = s.maxSubArray(nums)
    print(result)


# run57()


# 66. 加一
# https://leetcode-cn.com/problems/plus-one/
class Solution:
    def plusOne(self, digits):
        sum_num = 0
        result = []
        for index, num in enumerate(reversed(digits)):
            sum_num += num * 10 ** index
        sum_num += 1
        for char in str(sum_num):
            result.append(int(char))
        return result

    # 最优解
    def plusOne(self, digits):
        i = 1
        while (i <= len(digits)):
            if digits[-i] == 9:
                digits[-i] = 0
                i += 1
            else:
                digits[-i] += 1
                break
        # 判断整体进了一位之后
        if i == len(digits) + 1:
            digits = [1] + digits
        return digits


def run66():
    s = Solution()
    result = s.plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3])
    print(result)


# run66()


# 217. 存在重复元素
# https://leetcode-cn.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums):
        if not nums or len(nums) == 0:
            return True
        num_dict = {}
        max_num = 0
        for num in nums:
            num_dict[num] = num_dict.get(num, 0)
            max_num = max(max_num, num_dict[num])
            if max_num > 1:
                return True
        return False


# 219. 存在重复元素 II
# https://leetcode-cn.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        num_dict = {}
        for index, num in enumerate(nums):
            num_dict[num] = num_dict.get(num, [])
            num_dict[num].append(index)
            print(num_dict[num])
            if len(num_dict[num]) > 1 and (
                num_dict[num][len(num_dict[num]) - 1] - num_dict[num][len(num_dict[num]) - 2]) <= k:
                return True
        return False


def run219():
    s = Solution()
    result = s.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(result)


# run219()

# 220. 存在重复元素 III
# https://leetcode-cn.com/problems/contains-duplicate-iii/
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if not nums or len(nums) == 0:
            return False
        num_dict = {}
        # for index, num in enumerate(nums):
        #     num_dict[num] = num_dict.get(num, [])
        #     num_dict[num].append(index)
        #     print(num_dict[num])
        #     if len(num_dict[num]) > 1 and (num_dict[num][len(num_dict[num])-1] - num_dict[num][len(num_dict[num])-2]) <= k and
        #         num_dict[num]:
        #         pass
        #         return True
        return False


# 268. 缺失数字
# https://leetcode-cn.com/problems/missing-number/
class Solution:
    # 0.99%
    def missingNumber(self, nums) -> int:
        max_num = max(nums)
        for num in range(max_num + 1):
            if num not in nums:
                return num
        return max_num + 1

    # 最优解
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = sum(list(range(n + 1)))
        return s - sum(nums)


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_list = []
        for index, num in enumerate(nums):
            if num == 0:
                zero_list.append(index)
                nums.append(0)
        for index in zero_list:
            nums.pop(index)
        return nums


# 485. 最大连续1的个数
# https://leetcode-cn.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        result = 0
        max_num = 0
        for num in nums:
            if num == 1:
                result += 1
            else:
                max_num = max(max_num, result)
                result = 0
        max_num = max(max_num, result)
        return max_num
    # 最优解
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        Max = 0
        for i in nums:
            if i:
                count += 1
            else:
                if count > Max:
                    Max = count
                count = 0

        return Max if Max > count else count


def run485():
    s = Solution()
    result = s.findMaxConsecutiveOnes([1])
    print(result)
run485()

# 661. 图片平滑器
# https://leetcode-cn.com/problems/image-smoother/
class Solution:
    def imageSmoother(self, M) -> List[List[int]]:



