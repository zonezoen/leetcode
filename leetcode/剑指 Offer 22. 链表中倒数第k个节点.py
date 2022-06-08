# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        link_num = 0
        tmp_head = head
        while tmp_head:
            link_num += 1
            tmp_head = tmp_head.next
        tmp_head = head
        for index in range(link_num -k):
            tmp_head = tmp_head.next
        return tmp_head.next


