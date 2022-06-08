# Definition for a binary tree node.
# https://leetcode-cn.com/problems/path-sum/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        left_result = self.hasPathSum(root.left, targetSum - root.val)
        right_result = self.hasPathSum(root.right, targetSum - root.val)
        return left_result or right_result
