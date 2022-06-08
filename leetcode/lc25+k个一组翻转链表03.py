# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tmp_head = ListNode(-1)
        tmp_head.next = head
        pre = tmp_head
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return tmp_head.next

            next_node = tail.next
            head,tail = self.revers(head, tail)
            pre.next = head
            tail.next = next_node
            pre = tail
            head = next_node

        return tmp_head.next

    def revers(self,head:ListNode,tail:ListNode):
        pre = tail.next
        tmp_head = head
        while pre != tail:
            next_node = tmp_head.next
            tmp_head.next = pre
            pre = tmp_head
            tmp_head = next_node
        return tail,head

