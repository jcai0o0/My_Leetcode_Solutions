class Solution_1:
    def detectCapitalUse(self, word: str) -> bool:
        temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cnt = 0
        first_letter = 0
        for i in range(len(word)):
            if i == 0 and word[i] in temp:
                first_letter = 1
                cnt += 1
            elif word[i] in temp:
                cnt += 1
        if cnt == len(word) or cnt == 0 or (cnt == 1 and first_letter == 1):
            return True
        else:
            return False

class Solution_2:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        cap1 = word[1]
        for c in word[2:]:
            if c.islower() != cap1.islower():
                return False
        if word[0].islower() and cap1.isupper():
            return False
        return True