class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A==B:
            seen = set()
            for char in A:
                if char in seen:
                    return True
                seen.add(char)
            return False
        pair = []
        for i in range(len(A)):
            if A[i] != B[i]:
                pair.append((A[i], B[i]))
        if len(pair) > 2:
            return False
        return len(pair)==2 and pair[0] == pair[1][::-1]