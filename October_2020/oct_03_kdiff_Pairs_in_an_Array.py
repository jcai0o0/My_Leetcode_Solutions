class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        plus = {}
        minus = {}
        res = 0
        seen = set()
        for num in nums:
            if num in plus:
                if (num - k, num) not in seen:
                    res += plus[num]
                    seen.add((num - k, num))
            if num in minus:
                if (num, num + k) not in seen:
                    res += minus[num]
                    seen.add((num, num + k))

            if num + k not in plus:
                plus[num + k] = 1
            if num - k not in minus:
                minus[num - k] = 1
        return res

class Solution_clean:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        res = set()
        for num in nums:
            if num+k in d:
                res.add((num, num+k))
            if num-k in d:
                res.add((num-k, num))
            d[num] = 1
        return len(res)