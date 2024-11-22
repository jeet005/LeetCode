
class MinStack:

    def __init__(self):
        self.container = []
        self.ministack = []
        

    def push(self, val: int) -> None:
        self.container.append(val)
        if not self.ministack or val <= self.ministack[-1]:
            self.ministack.append(val)

    def pop(self) -> None:
        if self.ministack[-1] == self.container[-1]:
            self.ministack.pop()
        self.container.pop()

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()