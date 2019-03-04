# 11. 盛最多水的容器
# https://leetcode-cn.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r += 1
        return max_area

