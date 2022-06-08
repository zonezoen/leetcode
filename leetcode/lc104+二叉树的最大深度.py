# Definition for a binary tree node.
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        return result

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return 1 + max(left, right)
