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
                index += 1
            elif nums[index] == 0:
                zero += 1
                self.swap(nums[zero], nums[index])
                index += 1
            elif nums[index] == 2:
                two -= 1
                self.swap(nums[index], nums[two])

    def swap(self, num1, num2):
        num1 = num2
        num2 = num1


'''
冒泡排序：n^2
选择排序：n^2
插入排序：n^2
希尔排序：nlog n
归并排序：nlog n
快速排序：nlog n
    快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定
    等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。
堆排序：nlog n
计数排序：n+k
桶排序：n+k
基数排序：n*k
4、2、9、7、1、5、0
'''


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


nums = [3, 1, 6, 8, 3, 5, 0]

# 冒泡排序
'''
遍历，大的数字往后面冒
'''


def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)


# bubble_sort(nums)

# 选择排序
'''
选择一个最小的数，与第一位交换位置
'''


def select_sort(nums):
    length = len(nums)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if nums[min_index] > nums[j]:
                min_index = j
        if i != min_index:
            swap(nums, i, min_index)

# select_sort(nums)


# 插入排序
'''
遍历数组，每遍历得到一个数，与前面的有序部分比较，比较小的话，就往前面的有序部分插入
'''
def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                swap(nums, j - 1, j)

insert_sort(nums)



# 快速排序
def quick_sort(nums, left=None, right=None):
    pass


print(nums)


