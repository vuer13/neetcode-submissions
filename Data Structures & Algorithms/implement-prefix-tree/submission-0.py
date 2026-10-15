class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.curr = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.curr

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.curr

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.curr

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True
        