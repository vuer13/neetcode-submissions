class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1 for _ in range(n)] for _ in range(m)]
        print(grid)

        for i in range(m):
            grid[i][0] = 1
        for j in range(n):
            grid[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == -1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        print(grid)

        return grid[m-1][n-1]