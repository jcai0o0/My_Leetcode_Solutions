class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:
        if not self.arr:
            self.arr.append((x, x))
        else:
            self.arr.append((x, min(x, self.arr[-1][1])))

    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        if not self.arr:
            return None
        x, _ = self.arr[-1]
        return x

    def getMin(self) -> int:
        if not self.arr:
            return None
        _, x = self.arr[-1]
        return x

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()