# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        my_dict = {}
        tmp_head = ListNode(-101, head)
        while tmp_head:
            my_dict[tmp_head.val] = my_dict.get(tmp_head.val, 0) + 1
            tmp_head = tmp_head.next
        tmp_head = ListNode(-1, head)
        pre = tmp_head
        cur = tmp_head
        while cur:
            if my_dict.get(cur.val, 0) > 1:
                pre.next = cur.next
                # 跳过 node_x 之后，cur 等于 node_x.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return tmp_head.next

