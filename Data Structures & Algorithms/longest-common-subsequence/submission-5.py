class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if text2[i] == text1[j]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i][j-1], grid[i-1][j])

        print(grid)

        return grid[m-1][n-1]
