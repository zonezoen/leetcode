# Definition for a binary tree node.
# https://leetcode-cn.com/problems/binary-tree-right-side-view
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        self.right(root, result, 0)
        final_result = []
        for item_list in result:
            final_result.append(item_list[-1])
        return final_result

    def right(self, root: TreeNode, result: List, depth: int):
        if not root:
            return []
        if len(result) == depth:
            result.append([])
        result[depth].append(root.val)
        if root.left:
            self.right(root.left, result, depth + 1)
        if root.right:
            self.right(root.right, result, depth + 1)
