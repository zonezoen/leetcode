# https://leetcode-cn.com/problems/symmetric-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass

    def dfs(self,root:TreeNode):
        if not root:
            return
        left = self.dfs(root.left,root.right)
        right = self.dfs(root.right)