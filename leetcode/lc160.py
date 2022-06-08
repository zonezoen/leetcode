# Definition for singly-linked list.
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        tmp_head_a = headA
        tmp_head_b = headB
        while tmp_head_a != tmp_head_b:
            tmp_head_a = tmp_head_a.next if tmp_head_a else headB
            tmp_head_b = tmp_head_b.next if tmp_head_b else headA
        return tmp_head_a

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if headA is None or headB is None:
#             return None
#         tmp_list = []
#         tmp_head = ListNode(-1,headA)
#         tmp_head_b = ListNode(-1,headB)
#         while tmp_head.next:
#             tmp_list.append(tmp_head.next)
#             tmp_head = tmp_head.next
#         while tmp_head_b.next:
#             if tmp_head_b.next in tmp_list:
#                 return tmp_head_b.next
#             tmp_head_b = tmp_head_b.next
#         return None
# 8
# [4,1,8,4,5]
# [5,6,1,8,4,5]
# 2
# 3