# Definition for a binary tree node.
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.zigzag(root, result, 0)
        for index, item in enumerate(result):
            if index % 2 == 0:
                left = 0
                right = len(item) - 1
                while left < right:
                    item[left], item[right] = item[right], item[left],
                    left += 1
                    right -= 1
        return result

    def zigzag(self, root: TreeNode, result: List, depth: int):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root.val)
        self.zigzag(root.left, result, depth + 1)
        self.zigzag(root.right, result, depth + 1)

    # 解法 2
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.zigzag(root, result, 0)

        return result

    def zigzag(self, root: TreeNode, result: List, depth: int):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        if depth % 2 == 1:
            result[depth].insert(0, root.val)
        else:
            result[depth].append(root.val)
        self.zigzag(root.left, result, depth + 1)
        self.zigzag(root.right, result, depth + 1)


if __name__ == '__main__':
    que = collections.deque([])
    que.append(1)
    que.append(2)
    # que.appendleft(3)
    # que.appendleft(4)
    print(list(que))
