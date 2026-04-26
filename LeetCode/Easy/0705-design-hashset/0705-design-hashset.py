class MyHashSet:
    def __init__(self):
        self.NUM_BUCKETS = 1000
        self.buckets = [[] for _ in range(self.NUM_BUCKETS)]

    def _hash(self, key: int) -> int:
        return key % self.NUM_BUCKETS

    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.buckets[self._hash(key)]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)