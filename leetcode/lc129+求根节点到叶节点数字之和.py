# Definition for a binary tree node.
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0
    weishu_list = []

    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root,0)

    # 自上而下，把高位的值传递下去
    def dfs(self, root: TreeNode, top_num):
        if not root:
            return 0
        tmp_num = top_num * 10 + root.val
        # 遇到叶子节点就返回 tmp_num 
        if root.left is None and root.right is None:
            return tmp_num
        left = self.dfs(root.left, tmp_num)
        right = self.dfs(root.right, tmp_num)
        return left + right
