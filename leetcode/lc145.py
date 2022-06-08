# Definition for a binary tree node.
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.postor(root,ret)
        return ret

    def postor(self, root: TreeNode, result: List):
        if not root:
            return
        self.postor(root.left, result)
        self.postor(root.right, result)
        result.append(root.val)
