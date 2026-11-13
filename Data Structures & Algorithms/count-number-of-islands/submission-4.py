class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COLUMN = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(x, y):
            grid[x][y] = '0'

            queue = deque()
            queue.append((x, y))
            while queue:
                i, j = queue.popleft()
                for dx, dy in DIRECTIONS:
                    m, n = i + dx, j + dy
                    if (
                        m < 0
                        or n < 0
                        or m == ROW
                        or n == COLUMN
                        or grid[m][n] == '0'
                    ):
                        continue
                    grid[m][n] = '0'
                    queue.append((m, n))

        islands = 0
        for i in range(ROW):
            for j in range(COLUMN):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1

        return islands
    