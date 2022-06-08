# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        child_k_list = []
        child_result = []
        node_num = 0
        while head:
            head_next = head
            if node_num % k ==0:
                child_k_list.append(head)
            if node_num % k == 1:
                head.next = None
            node_num += 1
            head = head_next

        for child_k in child_k_list:
            child_head,child_tail = self.reverseChild(child_k)
            child_result.append((child_head,child_tail))
        pre_tail = None
        for index,result_item in enumerate(child_result):
            new_head,new_tail = result_item
            if index + 1 < len(child_result) -1:
                new_tail.next = child_result[index+1][0]
        return child_result[0][0]


    def reverseChild(self, head: ListNode) -> (ListNode, ListNode):
        if not head.next:
            return head, None
        pre = None
        tail = head
        while head:
            head_next = head.next
            head.next = None
            pre = head
            head = head_next
        return pre, tail

if __name__ == '__main__':
    t = (1,2)
    print(t[0])