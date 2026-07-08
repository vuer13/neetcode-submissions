class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        area = 0

        def dfs(i, j):
            if (
                i < 0 or j < 0 or i >= m or 
                j >= n or grid[i][j] == 0
            ):
                return 0
            
            grid[i][j] = 0
            islandArea = 1

            for dx, dy in directions:
                x, y = dx + i, dy + j
                islandArea += dfs(x, y)

            return islandArea
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currArea = dfs(i, j)
                    area = max(area, currArea)

        return area