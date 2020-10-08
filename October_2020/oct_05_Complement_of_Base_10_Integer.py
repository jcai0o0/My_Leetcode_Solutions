class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join(map(lambda x :"0" if x == "1" else "1", bin(N)[2:])), 2)