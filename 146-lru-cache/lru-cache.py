class LRUCache:

    def __init__(self, capacity: int):
        self.seen = Counter()
        self.maxx = capacity
        self.recent = deque()
        return 

    def get(self, key: int) -> int:
        if key in self.seen:
            self.recent.remove(key)
            self.recent.append(key)
            return self.seen[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.seen:
            self.seen[key] = value
            self.recent.remove(key)
            self.recent.append(key)
            return 
        if len(self.seen)  == self.maxx:
            old = self.recent.popleft()
            del self.seen[old]

        self.seen[key] = value
        self.recent.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)