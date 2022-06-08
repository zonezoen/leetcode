# Definition for singly-linked list.
# https://leetcode-cn.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast,slow = head,head
        while True:
            # if not (fast and fast.next):return
            if fast is None or fast.next is None:return
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tmp_list = []
        tmp_head = head
        while tmp_head:
            if tmp_head not in tmp_list:
                tmp_list.append(tmp_head)
            else:
                return tmp_head
            tmp_head = tmp_head.next
        return None