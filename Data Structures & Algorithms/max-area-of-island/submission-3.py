class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        area = 0

        def bfs(i, j):
            grid[i][j] = 0
            islandArea = 1
            queue = deque()
            queue.append((i, j))

            while queue:
                r, s = queue.popleft()
                for dx, dy in directions:
                    x, y = dx + r, dy + s
                    if (
                        x < 0 or y < 0 or x >= m or 
                        y >= n or grid[x][y] == 0
                    ):
                        continue
                    islandArea += 1
                    grid[x][y] = 0
                    queue.append((x, y))

            return islandArea
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    currArea = bfs(i, j)
                    area = max(area, currArea)

        return area