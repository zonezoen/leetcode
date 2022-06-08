# Definition for a binary tree node.
# https://leetcode-cn.com/problems/balanced-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    is_balance = True

    def isBalanced(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.is_balance

    def dfs(self, root: TreeNode):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left - right) > 1:
            self.is_balance = False
        return 1 + max(left, right)
