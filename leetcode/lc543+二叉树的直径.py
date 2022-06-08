# Definition for a binary tree node.
# https://leetcode-cn.com/problems/diameter-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_result = -1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        # 最开始 self.max_result 记录的是经过的节点数
        # 题目要求是两个节点之间的连线的数量，即是 节点总数 减去 1
        return self.max_result - 1

    def dfs(self, root: TreeNode, ):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max_result = max(self.max_result, left + right + 1)
        return 1 + max(left, right)
