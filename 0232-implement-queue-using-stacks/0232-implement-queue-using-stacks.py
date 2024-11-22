class MyQueue:

    def __init__(self):
        self.buffer = []

    def push(self, x: int) -> None:
        self.buffer.insert(0, x)
        
    def pop(self) -> int:
        return self.buffer.pop()
        
    def peek(self) -> int:
        return self.buffer[-1]
        
    def empty(self) -> bool:
        return len(self.buffer) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()