class Solution:
    def helper(self, A: str):
        A = list(A)
        f = s = 0
        while f < len(A):
            if s == 0 and A[f] != '#':
                A[s] = A[f]
                s += 1
            elif s > 0 and A[f] == '#':
                s -= 1

            elif s > 0 and A[f] != '#':
                A[s] = A[f]
                s += 1
            f += 1
        return ''.join(A[:s])

    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.helper(S)
        T = self.helper(T)
        return S == T