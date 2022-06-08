# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head is None:
            return None
        if head and head.next is None:
            return head
        tmp_head = ListNode(-1)
        tmp_head.next = head
        index = 0
        child_head_pre, child_tail = tmp_head, tmp_head
        while index < left - 1:
            child_head_pre = child_head_pre.next
            index += 1
        child_head = child_head_pre.next
        for index in range(right):
            child_tail = child_tail.next
            pass
        child_head, child_tail = self.reverseChild(child_head, child_tail)
        child_head_pre.next = child_head

        return tmp_head.next

    def reverseChild(self, head: ListNode, tail: ListNode):
        if head.next is None:
            return head,tail
        pre = tail.next
        tmp_head = head
        while pre != tail:
            next_node = tmp_head.next
            tmp_head.next = pre
            pre = tmp_head
            tmp_head = next_node
        return tail, head