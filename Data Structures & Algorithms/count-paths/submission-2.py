class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1] * n for _ in range(m)]
        
        def uniquePathsHelper(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if grid[i][j] != -1:
                return grid[i][j]

            grid[i][j] = uniquePathsHelper(i + 1, j) + uniquePathsHelper(i, j + 1)
            return grid[i][j]
        
        return uniquePathsHelper(0, 0)