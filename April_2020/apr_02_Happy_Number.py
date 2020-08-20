class Solution:
    def isHappy(self, n: int) -> bool:
        check = set()
        while n != 1 and n not in check:
            check.add(n)
            sum = 0
            n = str(n)
            for char in n:
                char = int(char)
                sum += char * char
            n = sum
        return n == 1