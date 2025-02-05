class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        start = t - 3000
        end = t
        count = 0
        for i in self.requests:
            if i >= start and i <= end:
                count += 1

        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)