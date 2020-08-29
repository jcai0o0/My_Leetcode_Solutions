class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.len = combinationLength

        def bt(ans, subset, current_position, characters, N):
            if current_position == N:
                ans.append(subset[:])
                return
            bt(ans, subset, current_position + 1, characters, N)
            subset.append(characters[current_position])
            bt(ans, subset, current_position + 1, characters, N)
            subset.pop()
            return

        def combi(characters):
            ans, subset = [], []
            bt(ans, subset, 0, characters, len(characters))
            return ans

        self.comb = ["".join(x) for x in combi(characters) if len(x) == self.len][::-1]
        print(self.comb)

    def next(self) -> str:
        if not self.comb:
            return None
        return self.comb.pop(0)

    def hasNext(self) -> bool:
        if len(self.comb) > 0:
            return True
        else:
            return False