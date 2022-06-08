# https://leetcode-cn.com/problems/min-stack/
class LinkNode:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next


class MinStack:
    min_node = None

    def __init__(self):
        self.tmp_head = LinkNode("head")
        self.tail = LinkNode("tail")
        self.tmp_head.next = self.tail
        self.tail.pre = self.tmp_head
        self.size = 0

    def push(self, val: int) -> None:
        self.size += 1
        new_node = LinkNode(val)
        if self.min_node is None or self.min_node.val > val:
            self.min_node = new_node

        new_node.pre = self.tmp_head
        self.tmp_head.next.pre = new_node
        new_node.next = self.tmp_head.next
        self.tmp_head.next = new_node

    def pop(self) -> None:
        self.size -= 1
        self.tmp_head.next.next.pre = self.tmp_head
        self.tmp_head.next = self.tmp_head.next.next
        cur = self.tmp_head.next
        self.min_node = None
        for i in range(self.size):
            if self.min_node is None:
                self.min_node = cur
            elif self.min_node.val > cur.val:
                self.min_node = cur
            cur = cur.next

    def top(self) -> int:
        return self.tmp_head.next.val

    def getMin(self) -> int:
        if self.min_node:
            return self.min_node.val
