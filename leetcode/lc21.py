# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        tmp_head = ListNode(-1)
        pre = tmp_head
        while list1 or list2:
            if not list1:
                pre.next = list2
                break
            if not list2:
                pre.next = list1
                break
            if list1.val <= list2.val:
                next_list = list1.next
                pre.next = list1
                pre = pre.next
                list1 = next_list
            else:
                next_list = list2.next
                pre.next = list2
                pre = pre.next
                list2 = next_list
        return tmp_head.next



























    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        tmp_head1 = list1
        tmp_head2 = list2
        while tmp_head1:
            tmp_head1_next = tmp_head1.next
            tmp_head2_next = tmp_head2.next
            if tmp_head1.val >= tmp_head2.val:
                tmp_head2.next = tmp_head1
            else:
                tmp_head1.next = tmp_head2
