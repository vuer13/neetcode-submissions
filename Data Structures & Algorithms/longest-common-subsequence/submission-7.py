class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        substring = [[0 for _ in range(n)] for _ in range(m)]
        substring[0][0] = 1 if text1[0] == text2[0] else 0

        for i in range(1, m):
            substring[i][0] = 1 if text1[i] == text2[0] else substring[i - 1][0]

        for j in range(1, n):
            substring[0][j] = 1 if text1[0] == text2[j] else substring[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                if text1[i] == text2[j]:
                    substring[i][j] = 1 + substring[i - 1][j - 1]
                else:
                    substring[i][j] = max(substring[i - 1][j], substring[i][j - 1])

        return substring[m - 1][n - 1]
