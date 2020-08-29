class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = []

    def add(self, key: int) -> None:
        if key not in self.h:
            self.h.append(key)
        return

    def remove(self, key: int) -> None:
        if key in self.h:
            self.h.remove(key)
        return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.h:
            return True
        else:
            return False