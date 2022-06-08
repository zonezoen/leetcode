from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.backtracing(root, result, 0)
        real_result = [item[-1] for item in result]
        return real_result

    def backtracing(self, root: TreeNode, result: List, deep: int):
        if not root:
            return
        if len(result) == deep:
            result.append([])
        result[deep].append(root.val)
        self.backtracing(root.left, result, deep + 1)
        self.backtracing(root.right, result, deep + 1)

#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         first_item = strs[0]
#         index = 0
#         length = len(strs) - 1
#         result = ""
#         while True:
#             is_bread = False
#             for count_index, str_item in enumerate(strs):
#                 if first_item[index] != str_item[index]:
#                     is_bread = True
#                     break
#                 if count_index == length:
#                     result += str_item
#                     index += 1
#             if is_bread:
#                 break
#         return result
