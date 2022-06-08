class LinkNode:
    def __init__(self, key, val, pre=None, next=None):
        self.pre = pre
        self.next = next
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.catch = {}
        self.size = 0
        self.head = LinkNode(-1,0)
        self.tail = LinkNode(-1,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.catch:
            return -1
        self.move_to_top(self.catch.get(key))
        return self.catch.get(key).val

    def put(self, key: int, value: int) -> None:
        if key in self.catch:
            self.catch.get(key).val = value
            self.move_to_top(self.catch.get(key))
        else:
            node = LinkNode(key, value)
            self.catch[key] = node
            self.add_to_top(node)
            self.size += 1
            if self.size > self.capacity:
                remove_node = self.remove_tail()
                del self.catch[remove_node.key]
                self.size -= 1

    def add_to_top(self, node: LinkNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node


    def remove_node(self, node: LinkNode)-> LinkNode:
        node.next.pre = node.pre
        node.pre.next = node.next

    def move_to_top(self, node: LinkNode):
        self.remove_node(node)
        self.add_to_top(node)

    def remove_tail(self):
        if self.tail.pre is self.head:
            return
        true_tail = self.tail.pre
        self.tail.pre = true_tail.pre
        true_tail.pre.next = self.tail
        return true_tail


if __name__ == '__main__':
    # Your LRUCache object will be instantiated and called as such:
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # 缓存是 {1=1}
    lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    lRUCache.get(1)  # 返回 1
    lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.get(2)  # 返回 -1 (未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.get(1)  # 返回 -1 (未找到)
    lRUCache.get(3)  # 返回 3
    lRUCache.get(4)  # 返回 4
