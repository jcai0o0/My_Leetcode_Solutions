class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stones = {}
        for s in S:
            if s in stones:
                stones[s] += 1
            else:
                stones[s] = 1
        res = 0
        for j in J:
            if j in stones:
                res += stones[j]
        return res