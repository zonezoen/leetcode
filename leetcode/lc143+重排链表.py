# Definition for singly-linked list.
# https://leetcode-cn.com/problems/reorder-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        left, right = 0, len(node_list) - 1
        while left < right:
            node_list[left].next = node_list[right]
            left += 1
            if left == right:
                break
            node_list[right].next = node_list[left]
            right -= 1
        print(len(node_list))
        print(left)
        node_list[left].next = None
        return node_list[0]

if __name__ == '__main__':
    tmp_head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    tmp_head.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = ListNode(5)
    s = Solution()
    print("----- end --------")
    # while tmp_head:
    #     print(tmp_head.val)
    #     tmp_head = tmp_head.next
    print("----- end --------")
    ret = s.reorderList(tmp_head)
    print("----- end --------")
    while ret:
        print(ret.val)
        ret = ret.next
