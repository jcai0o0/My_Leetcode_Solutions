class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        if not stones:
            return 0
        s = [-1 * n for n in stones]
        heapify(s)
        while len(s) > 1:
            Y = -1 * heappop(s)
            X = -1 * heappop(s)
            if X == Y:
                continue
            elif X < Y:
                heappush(s, -1 *(Y-X))
        if len(s) == 1:
            return s[0] * -1
        else:
            return 0