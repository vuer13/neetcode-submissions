class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        result = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            result[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                result[i][j] += result[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    result[i][j] += result[i - 1][j - 1]


        return result[m][n]
