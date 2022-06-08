from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ret = []
        self.inorder(root,ret)

    def inorder(self, root: Optional[TreeNode], ret: List):
        if root.val:
            self.inorder(root.left)
            ret.append(root.val)
            self.inorder(root.right)
