class FirstUnique:

    def __init__(self, nums: List[int]):
        self._dict = {}
        for num in nums:
            if num in self._dict:
                self._dict[num] += 1
            else:
                self._dict[num] = 1

        self._queue = []
        for k, v in self._dict.items():
            if v == 1:
                self._queue.append(k)

    def showFirstUnique(self) -> int:
        if len(self._queue) == 0:
            return -1

        return self._queue[0]

    def add(self, value: int) -> None:
        if value in self._dict.keys():
            if self._dict[value] == 1:
                self._queue.remove(value)
            self._dict[value] += 1
        else:
            self._dict[value] = 1
            self._queue.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)