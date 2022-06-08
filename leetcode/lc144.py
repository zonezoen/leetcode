# Definition for a binary tree node.
from typing import Optional, List
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        self.preorder(root,ret)
        return ret

    def preorder(self, root: TreeNode, ret: List):
        if not root:
            return
        ret.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
