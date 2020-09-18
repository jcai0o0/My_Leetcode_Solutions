class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, comb = [], []
        self.bt(res, comb, 1, n, k, 9)
        return res

    def bt(self, res, comb, start, target, size, end):
        if size == 0:
            if target == 0:
                res.append(comb[:])
                return
            return
        if target < 0:
            return

        for t in range(start, end + 1):
            comb.append(t)
            self.bt(res, comb, t + 1, target - t, size - 1, end)
            comb.pop()