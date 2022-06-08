# Definition for a binary tree node.
from typing import Dict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        depth_dict = {"left":0,"right":0}
        pass

    def calDepth(self,root:TreeNode,depth:Dict):
        if not root:
            return
        self.calDepth(root.left,depth)
        self.calDepth(root.right,depth)
