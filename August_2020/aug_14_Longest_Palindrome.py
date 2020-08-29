class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        even = 0
        odd = []
        res = 0
        for k, v in freq.items():
            if v % 2 == 0:
                even += v
            else:
                odd.append(v)
        res += even
        if odd:
            m = max(odd)
            odd.remove(m)
            res += m
            for num in odd:
                res += (num - 1)
        return res