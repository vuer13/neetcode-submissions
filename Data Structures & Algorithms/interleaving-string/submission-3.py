class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m + n != len(s3):
            return False

        # Each square will represent, can i + j create the first s3[:i + j]
        interleave = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        interleave[0][0] = True # Can create empty string

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue

                if i > 0 and s3[i + j - 1] == s1[i - 1]:
                    interleave[i][j] = interleave[i - 1][j] or interleave[i][j]
                if j > 0 and s3[i + j - 1] == s2[j - 1]:
                    interleave[i][j] = interleave[i][j - 1] or interleave[i][j]

        return interleave[m][n]
