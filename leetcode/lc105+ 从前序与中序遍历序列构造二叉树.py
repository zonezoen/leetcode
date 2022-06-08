# Definition for a binary tree node.
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        in_right_index = inorder.index(preorder[0]) - 1
        left = self.buildTree(preorder[1:in_right_index + 2], inorder[0:in_right_index + 1])
        right = self.buildTree(preorder[1 + in_right_index + 1:], inorder[1 + in_right_index + 1:])
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    s.buildTree(preorder, inorder)
    # print(preorder[1:3])
