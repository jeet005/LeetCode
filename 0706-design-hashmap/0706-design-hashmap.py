class MyHashMap:

    def __init__(self):
        self.max = 10
        self.arr = [[] for x in range(self.max)]

    def put(self, key: int, value: int) -> None:
        h = key % self.max

        for idx, item in enumerate(self.arr[h]):
            if item[0] == key:
                self.arr[h][idx] = (key, value)  # Update the existing key
                return

        # If key doesn't exist, append a new key-value pair
        self.arr[h].append((key, value))
    
    def get(self, key: int) -> int:
        h = key % self.max
        for idx, item in enumerate(self.arr[h]):
            if item[0] == key:
                return item[1]
        return -1  # Return -1 if key not found
        

    def remove(self, key: int) -> None:
        h = key % self.max
        self.arr[h] = [item for item in self.arr[h] if item[0] != key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)