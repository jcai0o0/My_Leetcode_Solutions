class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        val = 0
        for n in s+t:
            val ^= ord(n)
        return chr(val)