class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x, y = len(grid[0]), len(grid)
        area = 0

        def bfs(grid, x, y):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            queue = [(x, y)]
            grid[y][x] = 0
            area = 1

            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    i, j = x + dx, y + dy
                    if 0 <= i < len(grid[0]) and 0 <= j < len(grid) and grid[j][i] == 1:
                        grid[j][i] = 0
                        queue.append((i, j))
                        area += 1

            return area, grid

        for i in range(x):
            for j in range(y):
                if grid[j][i] == 1:
                    newArea, grid = bfs(grid, i, j)
                    if newArea > area:
                        area = newArea
        
        return area