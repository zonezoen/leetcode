"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
# Definition for a Node.

执行用时：
56 ms
, 在所有 Python3 提交中击败了
46.43%
的用户
内存消耗：
16.4 MB
, 在所有 Python3 提交中击败了
15.09%
的用户
通过测试用例：
55 / 55
"""
from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        result_list = []
        self.child_connect(root, 0, result_list)
        for item_list in result_list:
            for index, item in enumerate(item_list):
                if index <= len(item_list) - 1:
                    item.next = item_list[index + 1]
                else:
                    item.next = None
        return root

    def child_connect(self, root: 'Node', depth: int, result: List):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root)
        self.child_connect(root.left, depth + 1, result)
        self.child_connect(root.right, depth + 1, result)


if __name__ == '__main__':
    for index, item in enumerate(range(4)):
        print(index, item)
