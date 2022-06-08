# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                return True
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = head
        j = head

        while j != None and j.next != None:
            i = i.next
            j = j.next.next

            if i == j:
                return True

        return False

        pass
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tmp_list = []
        while head:
            if head in tmp_list:
                return True
            tmp_list.append(head)
            head = head.next
        return False