class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        word = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        word[0][0] = 0

        for i in range(1, m + 1):
            word[i][0] = word[i - 1][0] + 1
        for j in range(1, n + 1):
            word[0][j] = word[0][j - 1] + 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    word[i][j] = word[i - 1][j - 1]
                else:
                    word[i][j] = min(word[i - 1][j] + 1, word[i][j - 1] + 1, word[i - 1][j - 1] + 1)

        return word[m][n]