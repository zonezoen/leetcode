# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        tail = None
        carry = 0
        while l1 or l2:
            if l1:
                n = l1.val
            else:
                n = 0
            if l2:
                m = l2.val
            else:
                m = 0
            sum = n + m + carry
            if head is None:
                head = tail = ListNode(sum % 10)
            else:
                tail.next = ListNode(sum%10)
                tail = tail.next
            carry = int(sum / 10)
            if l1 is not None:
                l1 =  l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            tail.next = ListNode(carry)
        return head

# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         num_10 = 0
#         num_1 = 0
#         l1_head = l1
#         while l1 or l2:
#             # n = l1.val is not None ? l1.val:0
#             if l1.val:
#                 n = l1.val
#             else:
#                 n = 0
#             if l2.val:
#                 m = l2.val
#             else:
#                 m = 0
#             tmp_sum = n + m + num_10
#             num_1 = tmp_sum % 10
#             num_10 = tmp_sum // 10
#             l1.val = num_1
#             if l1.next is None and l2.next:
#                 l1.next = l2.next
#                 l1.next.val += num_10
#                 break
#             if l2.next is None and l1.next:
#                 l1.next.val += num_10
#                 break
#             if l1.next is None and l2.next is None and num_10 > 0:
#                 l1.next = ListNode(num_10)
#                 break
#             l1 = l1.next
#             l2 = l2.next
#         return l1_head
