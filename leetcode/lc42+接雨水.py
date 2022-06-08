from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        leftMax = [height[0]]
        for i in range(1, length):
            tmp_max = max(leftMax[-1], height[i])
            leftMax.append(tmp_max)
        print(leftMax)
        rightMax = [height[-1]]
        for i in range(length - 2, -1, -1):
            tmp_max = max(rightMax[0], height[i])
            rightMax.insert(0, tmp_max)
        print(rightMax)
        ans = 0
        for i in range(length):
            ans += min(leftMax[i],rightMax[i]) - height[i]
        return ans

    # 错误解法，未通过
    # def trap(self, height: List[int]) -> int:
    #     ans = 0
    #     last_max_height = height[0]
    #     last_max_height_index = 0
    #     ans_dict = {}
    #     for index, current_height in enumerate(height):
    #         if index - 1 > 0:
    #             if height[index - 1] >= last_max_height:
    #                 last_max_height = height[index - 1]
    #                 last_max_height_index = index - 1
    #         low_height = min(current_height, last_max_height)
    #         tmp_ans = 0
    #         if last_max_height_index < index:
    #             for tmp_index, tmp_height, in enumerate(height[last_max_height_index:index]):
    #                 if low_height == tmp_height:
    #                     tmp_ans = 0
    #                 if low_height - tmp_height > 0:
    #                     tmp_ans += low_height - tmp_height
    #         ans_dict[index] = tmp_ans
    #
    #         for tmp_index in range(last_max_height_index + 1, index):
    #             if current_height > height[tmp_index]:
    #                 print(height[tmp_index])
    #                 ans_dict[tmp_index] = 0
    #     print(ans_dict)
    #     print(last_max_height)
    #     print(last_max_height_index)
    #     for key, val in ans_dict.items():
    #         ans += val
    #     return ans


if __name__ == '__main__':
    aa = [4, 2, 0, 3, 2, 5]
    aa = [0,1,0,2,1,0,1,3,2,1,2,1]
    s = Solution()
    print(s.trap(aa))
