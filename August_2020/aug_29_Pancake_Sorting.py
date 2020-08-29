class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return []
        dic = {}
        for i in range(len(A)):
            dic[A[i]] = i

        def solve_index(idx):
            idx -= 1
            for k, i in dic.items():
                if i <= idx:
                    dic[k] = idx - i

        res = []
        m = max(A)
        while m > 1:
            idx = dic[m]
            if idx == m - 1:
                m -= 1
                continue
            res.append(idx + 1)
            solve_index(idx + 1)
            res.append(m)
            solve_index(m)
            m -= 1
        return res