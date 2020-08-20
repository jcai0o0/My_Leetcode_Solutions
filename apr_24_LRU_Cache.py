class LRUCache:

    def __init__(self, capacity: int):
        self._cache = collections.OrderedDict()
        self._maxsize = capacity

    def get(self, key: int) -> int:
        val = self._cache.get(key)
        if val:
            self._cache.move_to_end(key)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if self._cache.get(key):
            self._cache.move_to_end(key)
        elif len(self._cache) == self._maxsize:
            self._cache.popitem(last=False)
        self._cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)