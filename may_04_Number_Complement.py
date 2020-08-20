class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_set = set(ransomNote)
        for char in ransome_set:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True