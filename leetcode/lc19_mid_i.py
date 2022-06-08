# https://leetcode-cn.com/problems/binary-tree-right-side-view
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        num = 0
        while True:
            if not cur: break
            num += 1
            cur = cur.next
        # 之所以要用 new_head，是因为 head 也可以能被删除
        new_head = ListNode(-1, head)
        cur = new_head
        for index in range(num - n):
            cur = cur.next
        cur.next = cur.next.next
        return new_head.next


for index in range(3):
    print(index)
