class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x, y = len(grid[0]), len(grid) # number of items in row
        count = 0

        def bfs(grid, x, y):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            queue = [(x, y)]
            grid[y][x] = 0

            while queue:
                x, y = queue.pop(0)
                for dx, dy in directions:
                    i = x + dx
                    j = y + dy
                    if 0 <= i < len(grid[0]) and 0 <= j < len(grid) and grid[j][i] == "1":
                        grid[j][i] = "0"
                        queue.append((i, j))

            return grid

        for i in range(x):
            for j in range(y):
                if grid[j][i] == "1":
                    grid = bfs(grid, i, j)
                    count += 1

        return count
    