class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        result = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        result[0][0] = True

        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                result[i][0] = result[i - 1][0]

        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                result[0][j] = result[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    result[i][j] = result[i - 1][j] or result[i][j]
                if s2[j - 1] == s3[i + j - 1]:
                    result[i][j] = result[i][j - 1] or result[i][j]

        return result[m][n]