class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.find(self.root, word)

    def find(self, node, word):
        if word == "":
            return node.isWord
        if word[0] == ".":
            for x in node.children:
                if self.find(node.children[x], word[1:]):
                    return True
        else:
            child = node.children.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False