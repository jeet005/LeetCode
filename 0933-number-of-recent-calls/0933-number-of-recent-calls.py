class RecentCounter:
    
    def __init__(self):
        self.count = deque()
        self.cnt = 0  

    def ping(self, t: int) -> int:
        self.count.append(t)
        # Remove elements that are outside the range [t-3000, t]
        while self.count[0] < t - 3000:
            self.count.popleft()
        return len(self.count)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)