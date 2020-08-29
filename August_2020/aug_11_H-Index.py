class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations == [0]:
            return 0
        citations = sorted(citations)[::-1]
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)