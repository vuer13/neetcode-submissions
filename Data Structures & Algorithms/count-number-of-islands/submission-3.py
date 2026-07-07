class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque()
            grid[i][j] = '0'
            queue.append((i, j))

            while queue:
                row, col = queue.popleft()
                for dx, dy in directions:
                    x = row + dx
                    y = col + dy
                    if (x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == '0'):
                        continue
                    queue.append((x, y))
                    grid[x][y] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        
        return islands