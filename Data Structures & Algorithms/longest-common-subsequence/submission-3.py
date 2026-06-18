class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        if text1[0] == text2[0]:
            grid[0][0] = 1
        else:
            grid[0][0] = 0

        for i in range(1, m):
            if text2[i] == text1[0]:
                grid[i][0] = 1
            else:
                grid[i][0] = grid[i-1][0]

        for j in range(1, n):
            if text2[0] == text1[j]:
                grid[0][j] = 1
            else:
                grid[0][j] = grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == -1:
                    if text2[i] == text1[j]:
                        grid[i][j] = 1 + max(grid[i][j-1], grid[i-1][j])
                    else:
                        grid[i][j] = grid[i][j-1]

        print(grid)

        return grid[m-1][n-1]
