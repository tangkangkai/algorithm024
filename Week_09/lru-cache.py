class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key, last=True)
        return self.dict[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.capacity == 0:
                self.dict.popitem(last=False)
            else:
                self.capacity -= 1
        else:
            self.dict.move_to_end(key, last=True)
        self.dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)