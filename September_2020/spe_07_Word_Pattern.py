class Solution_1:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False
        arr = str.split(" ")
        if len(arr) != len(pattern):
            return False
        occur = collections.defaultdict(list)
        for i in range(len(pattern)):
            if pattern[i] in occur:
                occur[pattern[i]].append(i)
            else:
                occur[pattern[i]] = [i]
        # print(occur)
        seen = set()
        for v in occur.values():
            temp = arr[v[0]]
            if temp in seen:
                return False
            else:
                seen.add(temp)
            for i in v[1:]:
                if arr[i] != temp:
                    return False
        return True


class Solution_2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False

        words = str.split(" ")
        if len(words) != len(pattern):
            return False

        char_map = {}
        word_map = {}

        for char, word in zip(pattern, words):
            if char not in char_map:
                if word in word_map:
                    return False
                else:
                    char_map[char] = word
                    word_map[word] = char
            else:
                if char_map[char] != word:
                    return False

        return True