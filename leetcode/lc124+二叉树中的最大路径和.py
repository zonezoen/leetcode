# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, Dict


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = {}
        self.dfs(root, result)
        return result.get("max")

    def dfs(self, root: TreeNode, result: Dict):
        if not root:
            return 0

        left = self.dfs(root.left, result)
        right = self.dfs(root.right, result)
        ret = root.val + left + right
        ret_return = root.val + max(left, right)
        result["max"] = max(result.get("max", -1001), ret)
        if ret_return > 0:
            return ret_return
        else:
            return 0
