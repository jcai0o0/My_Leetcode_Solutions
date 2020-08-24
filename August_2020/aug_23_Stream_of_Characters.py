class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            temp = self.trie
            for char in word[::-1]:
                if char not in temp:
                    temp[char] = {}
                temp = temp[char]
            temp['#'] = True
        self.s = ''

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        temp = self.trie
        for char in self.s:
            if '#' in temp:
                return True
            elif char not in temp:
                return False
            else:
                temp = temp[char]
        return True if '#' in temp else False