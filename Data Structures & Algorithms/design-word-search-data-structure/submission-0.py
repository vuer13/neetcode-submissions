class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.curr = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.curr

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(start, curr):
            n = len(word)

            for i in range(start, n):
                char = word[i]
                if char == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]

            return curr.end
        
        return dfs(0, self.curr)
