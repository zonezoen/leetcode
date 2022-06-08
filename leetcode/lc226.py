# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.inver_child(root)
        return root

    def inver_child(self,root:TreeNode):
        if not root:
            return
        ritht = root.left
        left = root.right
        self.inver_child(ritht)
        self.inver_child(left)
        root.left = left
        root.right = ritht


