class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.curr = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.curr
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end = True

    def search(self, word: str) -> bool:
        def dfs(start, current):
            for i in range(start, len(word)):
                char = word[i]
                if char == '.':
                    for trie in current.children.values():
                        if dfs(i + 1, trie):
                            return True
                    return False
                else:
                    if char not in current.children:
                        return False
                    current = current.children[char]
                
            return current.end
        return dfs(0, self.curr)
