class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = []
        for i in range(1, 10):
            q = [str(i)]
            while len(q) > 0:
                item = q.pop(0)
                if len(item) == N:
                    res.append(item)
                    continue
                last = int(item[-1])
                if (last - K) >= 0:
                    q.append(item + str(last-K))
                if K != 0 and abs(last + K) < 10:
                    q.append(item + str(last + K))
        if N == 1:
            res.insert(0, '0')
        return [int(i) for i in res]