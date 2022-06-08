# https://leetcode-cn.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        left = 0
        right = len(head_list) - 1
        while left < right:
            if head_list[left] == head_list[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
