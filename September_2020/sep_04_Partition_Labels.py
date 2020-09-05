class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_indx = {}
        for i, char in enumerate(S):
            last_indx[char] = i
        start = end = 0
        res = []
        for i, char in enumerate(S):
            end = max(end, last_indx[char])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res