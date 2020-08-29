# two pointers - TC:O(n) SC:O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.lower()
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        left, right = 0, len(s)-1
        while left < right:
            if s[left] in letters and s[right] in letters:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if s[left] not in letters:
                    left += 1
                if s[right] not in letters:
                    right -= 1
        return True