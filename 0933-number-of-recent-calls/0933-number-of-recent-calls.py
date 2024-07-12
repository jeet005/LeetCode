class RecentCounter:
    
    def __init__(self):
        self.count = []        

    def ping(self, t: int) -> int:
        cnt = 0
        self.count.append(t)
        Crange = [t - 3000, t]
        
        for x in self.count:
            if x >= Crange[0] and x <= Crange[1]:
                cnt += 1

        return cnt
    
    def __repr__(self):
        return '[]'

        return cnt
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)