class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        res, comb = [], []
        candidates.sort()
        self.bt(candidates, target, res, comb, 0)
        return res

    def bt(self, candidates, target, res, comb, begin):
        if target == 0:
            res.append(comb[:])
            return
        for i in range(begin, len(candidates)):
            residue = target - candidates[i]
            if residue < 0:
                break
            comb.append(candidates[i])
            self.bt(candidates, residue, res, comb, i)
            comb.pop()
        return