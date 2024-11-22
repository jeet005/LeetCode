
class MinStack:

    def __init__(self):
        self.container = []
        

    def push(self, val: int) -> None:
        if not self.container:
            self.container.append((val, val))

        curr_min = self.container[-1][1]
        self.container.append((val, min(val, curr_min)))


    def pop(self) -> None:
        self.container.pop()
        

    def top(self) -> int:
        return self.container.pop()[0]
        

    def getMin(self) -> int:
        if self.container[-1][1]:
            return self.container[-1][1]
        else:
            []


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()