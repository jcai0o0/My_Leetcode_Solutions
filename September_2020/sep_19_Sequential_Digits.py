class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = list(range(1,10))
        while len(queue) > 0:
            val = queue.pop(0)
            if val >= low and val <= high:
                res.append(val)
            elif val > high:
                continue
            last = int(str(val)[-1])
            if last == 9:
                continue
            new_val = str(val) + str(last + 1)
            queue.append(int(new_val))
        return sorted(res)