# Definition for a binary tree node.
from typing import List
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ret = []
        self.level(root, 0, ret)
        return ret

    def level(self, root: TreeNode, depth: int, ret: List):
        if len(ret) == depth:
            ret.append([])
        ret[depth].append(root.val)
        if root.left:
            self.level(root.left, depth + 1, ret)
        if root.right:
            self.level(root.right, depth + 1, ret)
