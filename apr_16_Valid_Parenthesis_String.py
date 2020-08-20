class Solution:
    def checkValidString(self, s: str) -> bool:
        max_op, min_op = 0, 0
        for char in s:
            if char == '(':
                max_op += 1
                min_op += 1
            elif char == '*':
                max_op += 1
                min_op -= 1
            else:
                max_op -= 1
                min_op -= 1
            if min_op < 0:
                min_op = 0
            if max_op < 0:
                return False
        return min_op == 0