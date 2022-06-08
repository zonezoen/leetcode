# 正确
# https://leetcode-cn.com/problems/implement-queue-using-stacks/
# class MyQueue:
#
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def push(self, x: int) -> None:
#         self.s1.append(x)
#
#
#     def pop(self) -> int:
#         if not self.s2:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#         return self.s2.pop()
#
#
#     def peek(self) -> int:
#         if not self.s2:
#             while self.s1:
#                 self.s2.append(self.s1.pop())
#         return self.s2[-1]
#
#     def empty(self) -> bool:
#         return not self.s2 and not self.s1



# 正确
class MyQueue:

    def __init__(self):
        self.front= None
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if not self.s1:
            self.front = x
            self.s1.append(x)
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s1.append(x)
            while self.s2:
                self.s1.append(self.s2.pop())


    def pop(self) -> int:
        pop_num = self.s1.pop()
        if self.s1:
            self.front = self.s1[-1]
        else:
            self.front = None
        return pop_num


    def peek(self) -> int:
        return self.front

    def empty(self) -> bool:
        return False if self.s1 else True





# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.peek()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)