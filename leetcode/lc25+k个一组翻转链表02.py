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
            for index in range(k):
                tail = tail.next
                if not tail:
                    return tmp_head.next
            child_head, child_tail = self.reverseChild(head, tail)
            print(child_head.val)
            print(child_tail.val)
            pre.next = child_head
            child_tail.next = tail.next
            pre = child_tail
            head = child_tail.next


            nex = tail.next
            head, tail = self.reverseChild(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return tmp_head.next

    def reverseChild(self, head: ListNode, tail: ListNode) -> (ListNode, ListNode):
        pre = tail.next

        while head != tail:
            head_next = head.next
            head.next = pre
            pre = head
            head = head_next
        return tail, head


if __name__ == '__main__':
    t = (1, 2)
    print(t[0])
