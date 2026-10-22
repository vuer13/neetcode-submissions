class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        result = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            result[i][0] = result[i - 1][0] + 1

        for j in range(1, n2 + 1):
            result[0][j] = result[0][j - 1] + 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    result[i][j] = result[i - 1][j - 1]
                else:
                    result[i][j] = min(result[i - 1][j - 1], result[i][j - 1], result[i - 1][j]) + 1

        return result[n1][n2]