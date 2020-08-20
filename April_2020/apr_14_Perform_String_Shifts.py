class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        for i in shift:
            if i[0] == 0:
                s = s[i[1]:] + s[:i[1]]
            elif i[0] == 1:
                s = s[-i[1]:] + s[:-i[1]]
        return s