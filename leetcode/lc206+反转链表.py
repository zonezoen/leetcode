class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            head_next = head.next
            head.next = pre
            pre = head
            head = head_next



































    def reverseList(self, head: ListNode) -> ListNode:
        last_node = None
        while head:
            head_next = head.next
            head.next = last_node
            last_node = head
            head = head_next
        return last_node
